if(CURA_BUILDTYPE STREQUAL "")
    cpack_add_component(_cura
                DISPLAY_NAME "FOKOOS Slicer"
                Description "Ultimaker Cura Executable and Data Files"
                REQUIRED
    )
else()
    cpack_add_component(_cura
                DISPLAY_NAME "FOKOOS Slicer ${CURA_BUILDTYPE}"
                Description "FOKOOS Slicer ${CURA_BUILDTYPE} Executable and Data Files"
                REQUIRED
    )
endif()

# ========================================
# CPack Common Settings
# ========================================

if(CURA_BUILDTYPE STREQUAL "")
    set(CPACK_PACKAGE_NAME "FOKOOS Slicer")
else()
    set(CPACK_PACKAGE_NAME "FOKOOS Slicer ${CURA_BUILDTYPE}")
endif()
string(REPLACE " " "_" CPACK_FILE_NAME_NO_SPACES "${CPACK_PACKAGE_NAME}")

set(CPACK_PACKAGE_VENDOR "Ultimaker B.V.")
set(CPACK_PACKAGE_HOMEPAGE_URL "https://github.com/zlh6630/Cura")

# MSI only supports version format like "x.x.x.x" where x is an integer from 0 to 65534
set(CPACK_PACKAGE_VERSION_MAJOR ${CURA_VERSION_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR ${CURA_VERSION_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH ${CURA_VERSION_PATCH})

# Use full version x.x.x string in install directory for both installers,
# so that IT can easily automatically upgrade to a newer patch version,
# but also uninstall only the desired EXE installation. Also differentiate
# betweem build types
set(CURA_FULL_VERSION "${CURA_VERSION_MAJOR}.${CURA_VERSION_MINOR}.${CURA_VERSION_PATCH}")
if(CURA_BUILDTYPE STREQUAL "")
    set(CPACK_PACKAGE_NAME "FOKOOS Slicer ${CURA_FULL_VERSION}")
else()
    set(CPACK_PACKAGE_NAME "FOKOOS Slicer ${CURA_BUILDTYPE} ${CURA_FULL_VERSION}")
endif()

set(CPACK_PACKAGE_ICON "${CMAKE_SOURCE_DIR}/packaging/cura.ico")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "FOKOOS Slicer - 3D Printing Software")
set(CPACK_PACKAGE_CONTACT "Ruben Dulek <r.dulek@ultimaker.com>")
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_SOURCE_DIR}/packaging/cura_license.txt")

# Differentiate between a normal Cura installation and that of a different build type
if(CURA_BUILDTYPE STREQUAL "")
    set(CPACK_CREATE_DESKTOP_LINKS Cura "FOKOOS Slicer ${CURA_FULL_VERSION}")
    set(CPACK_PACKAGE_EXECUTABLES Cura "FOKOOS Slicer ${CURA_FULL_VERSION}")
    set(CPACK_PACKAGE_INSTALL_DIRECTORY "FOKOOS Slicer ${CURA_FULL_VERSION}")
else()
    set(CPACK_CREATE_DESKTOP_LINKS Cura "FOKOOS Slicer ${CURA_BUILDTYPE} ${CURA_FULL_VERSION}")
    set(CPACK_PACKAGE_EXECUTABLES Cura "FOKOOS Slicer ${CURA_BUILDTYPE} ${CURA_FULL_VERSION}")
    set(CPACK_PACKAGE_INSTALL_DIRECTORY "FOKOOS Slicer ${CURA_BUILDTYPE} ${CURA_FULL_VERSION}")
endif()

# Use processor name
STRING(TOLOWER "${CMAKE_SYSTEM_PROCESSOR}" CPACK_SYSTEM_NAME)
set(CPACK_PACKAGE_FILE_NAME "${CPACK_FILE_NAME_NO_SPACES}-${CURA_VERSION}-${CPACK_SYSTEM_NAME}")
