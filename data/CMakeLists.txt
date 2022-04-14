
option(INCLUDE_WORDLISTS "Include wordlists files" OFF)
set(CMAKE_CURRENT_WORDLISTS_DIR ${CMAKE_CURRENT_BINARY_DIR}/wordlists)
include(ExternalProject)
if(INCLUDE_WORDLISTS)
  set(EP_SECLISTS "seclists")
  ExternalProject_Add(seclists
    GIT_REPOSITORY https://github.com/danielmiessler/SecLists.git
    GIT_PROGRESS ON
    PREFIX ${EP_SECLISTS}
    DOWNLOAD_DIR ${CMAKE_CURRENT_WORDLISTS_DIR}/${EP_SECLISTS}
    INSTALL_COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_CURRENT_WORDLISTS_DIR}/${EP_SECLISTS} ${AMACONTROLLER_WORDLISTS_DIR}
  )
endif()
