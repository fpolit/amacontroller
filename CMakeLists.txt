cmake_minimum_required(VERSION 3.5)

project(amacontroller
  VERSION 1.0.0
  DESCRIPTION "Ama-Framework controller"
  HOMEPAGE_URL https://github.com/fpolit/amacontroller
)

set(CMAKE_CXX_STANDARD 11)
set(PROJECT_LICENSE "GPLv3")
option(CMAKE_COMPILER_WALL "Warning all" ON)
option(CMAKE_BUILD_TESTS  "Build unittest" OFF)

if(CMAKE_COMPILER_WALL)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")
endif()

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  message(DEBUG "Adding -ggdb compiler flag")
  set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -ggdb" CACHE STRING "gdb debug support" FORCE)
endif()


# amacontroller config file
set(AMACONTROLLER_CONFIG_FILE "${CMAKE_CURRENT_BINARY_DIR}/ama.conf")
set(AMACONTROLLER_CONFIG_FILE_IN "${CMAKE_CURRENT_SOURCE_DIR}/data/ama.conf.in")
configure_file(${AMACONTROLLER_CONFIG_FILE_IN} ${AMACONTROLLER_CONFIG_FILE})
install(FILES ${AMACONTROLLER_CONFIG_FILE} DESTINATION /etc PERMISSIONS OWNER_WRITE OWNER_READ)


# AMACONTROLLER_SHARE_DIR structure
# AMACONTROLLER_
# |- resources (git repository of registered resources [wordlists, masks, rules, ...])
# |  |- wordlists
# |  |- masks
# |  |- rules
# |
# |- workspaces
# |  |- WORKSPACE_ID
# |  |  |- JOB_ID
# |  |  |  |- OUTPUT FILES (generated files by amaprocessor nodes)


set(AMACONTROLLER_SHARE_DIR "/usr/share/${PROJECT_NAME}" CACHE STRING "")
set(AMACONTROLLER_RESOURCES_DIR "${AMACONTROLLER_SHARE_DIR}/resources" CACHE STRING "")
set(AMACONTROLLER_WORDLISTS_DIR "${AMACONTROLLER_RESOURCES_DIR}/wordlists" CACHE STRING "")


# find_package(Boost COMPONENTS program_options REQUIRED)
# if(CMAKE_BUILD_PYBINDS)
#   find_package(Boost COMPONENTS python REQUIRED)
# endif()

## enviroment INFO
message(DEBUG "PROJECT_VERSION: ${CMAKE_PROJECT_VERSION}")
message(DEBUG "CMAKE_BUILD_TYPE: ${CMAKE_BUILD_TYPE}")
message(DEBUG "CMAKE_BUILD_TESTS: ${CMAKE_BUILD_TESTS}")
message(DEBUG "GIT_UPDATE_SUBMODULES: ${GIT_UPDATE_SUBMODULES}")
message(DEBUG "CMAKE_CURRENT_SOURCE_DIR: ${CMAKE_CURRENT_SOURCE_DIR}")
message(DEBUG "CMAKE_CURRENT_BINARY_DIR: ${CMAKE_CURRENT_BINARY_DIR}")


# Updating git submodules
option(GIT_UPDATE_SUBMODULES "Check submodules during build" OFF)

if(GIT_UPDATE_SUBMODULES)
  find_package(Git REQUIRED)
  # initializing submodules
  execute_process(COMMAND ${GIT_EXECUTABLE} submodule update --init --recursive
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    RESULT_VARIABLE GIT_SUBMODULE_RESULT
  )
  if(NOT GIT_SUBMODULE_RESULT EQUAL "0")
    message(FATAL_ERROR "git submodule update --init --recursive failed with ${GIT_SUBMODULE_INIT_RESULT}")
  endif()
endif()

# protobuf files
set(CMAKE_BUILD_AMACONTROLLER_CXX_PROTO ON CACHE BOOL "Build amacontroller protobuf files")
add_subdirectory(proto) # generate amacontroller_cxx_protos library

# amacontroller library
# file(GLOB AMACORE_SRC src/*.cpp)
# message(DEBUG "Source code: ${AMACORE_SRC}")

# add_library(amacontroller SHARED ${AMACORE_SRC})

# target_include_directories(amacontroller
#   PUBLIC
#   ${PROJECT_SOURCE_DIR}/include/
# )

# tests
if(CMAKE_BUILD_TESTS)
  enable_testing()
  add_subdirectory(tests)
endif()

add_subdirectory(data)
