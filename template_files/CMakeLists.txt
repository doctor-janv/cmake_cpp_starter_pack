cmake_minimum_required(VERSION 3.28)

#================================================ Set variables
set(APP_NAME "tttAppNamettt")

message(STATUS "Configuring ${CMAKE_BUILD_TYPE} build of tttAppNamettt.")

project(${APP_NAME} LANGUAGES CXX)

#================================================ Set cmake variables
# This section sets cmake to create binaries in bin/lib
if (NOT DEFINED CMAKE_RUNTIME_OUTPUT_DIRECTORY)
    set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_LIST_DIR}/lib")
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_LIST_DIR}/lib")
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_LIST_DIR}/bin")

    set(CONFIG_FILE_NAME "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/config.cmake")
    file(WRITE "${CONFIG_FILE_NAME}"
        "# Environment configuration file for ${tttAppNamettt}.\n")
endif()

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CXX_SCAN_FOR_MODULES TRUE)

#================================================ Export vars to config file

#================================================ Include macros
# include(GNUInstallDirs)

#================================================ Set header include directories

#================================================ Set library directories

#================================================ Set library list
set(APP_LIB_LIST)

#================================================ Compiler flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fmodules-ts")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -O0 -fmodules-ts")

set(APP_CXX_FLAGS)
if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    list(APPEND APP_CXX_FLAGS "-pedantic")
    list(APPEND APP_CXX_FLAGS "-Wall")
    list(APPEND APP_CXX_FLAGS "-Wno-unused-variable")
elseif(CMAKE_CXX_COMPILER_ID MATCHES "AppleClang")
    list(APPEND APP_CXX_FLAGS "-pedantic")
    list(APPEND APP_CXX_FLAGS "-Wall")
    list(APPEND APP_CXX_FLAGS "-Wno-unused-variable")
elseif("${CMAKE_CXX_COMPILER_ID}" MATCHES "GNU")
    list(APPEND APP_CXX_FLAGS "-pedantic")
    list(APPEND APP_CXX_FLAGS "-Wall")
    list(APPEND APP_CXX_FLAGS "-Wno-unused-variable")
    list(APPEND APP_CXX_FLAGS "-Wno-sign-compare")
    list(APPEND APP_CXX_FLAGS "-Wno-psabi")
else()
    message(WARNING "Untested CMAKE_CXX_COMPILER_ID : ${CMAKE_CXX_COMPILER_ID}")
endif()

#================================================ Linker flags
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")

#================================================ Third-party library

#================================================ Define sources
set(CXX_SOURCES "${CMAKE_CURRENT_LIST_DIR}/src/tttAppNamettt.cpp")

#================================================ Define targets
add_executable(${APP_NAME} ${CXX_SOURCES})

target_link_libraries(${APP_NAME} ${APP_LIB_LIST})

# |------------ Write Makefile to root directory
file(WRITE ${PROJECT_SOURCE_DIR}/Makefile "subsystem:\n" "\t$(MAKE) -C cmake-build \n\n"
        "clean:\n\t$(MAKE) -C cmake-build clean\n")
