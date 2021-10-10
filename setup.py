#  Needed build-ins
import sys
import os.path
import platform

# Importing preinstalled modules to get their paths
import PyQt5
import numpy
import trimesh
import shapely

from cx_Freeze import setup, Executable, hooks


zip_includes = []


def load_numpy(finder, module):
    finder.IncludePackage("numpy.core._methods")
    finder.IncludePackage("numpy._globals")
    finder.IncludePackage("numpy.lib.format")
    finder.IncludePackage("numpy.linalg._umath_linalg")

    # Include all MKL files that are needed to get Numpy with MKL working.
    npy_core_dir = os.path.join(module.path[0], "core")
    required_mkl_files = [
        "mkl_intel_thread.dll",
        "mkl_core.dll",
        "mkl_avx.dll",
        "mkl_avx2.dll",
        "libiomp5md.dll",
        "libimalloc.dll",
        "libmmd.dll",
        "libifcoremd.dll",
    ]

    if platform.architecture()[0] == "32bit":
        required_mkl_files.extend([
            "mkl_p4.dll",
            "mkl_p4m.dll",
            "mkl_p4m3.dll",
        ])
    else:
        required_mkl_files.extend([
            "mkl_def.dll",
            "mkl_mc.dll",
            "mkl_mc3.dll",
        ])

    for file in required_mkl_files:
        finder.IncludeFiles(os.path.join(npy_core_dir, file), file)

hooks.load_numpy = load_numpy

def load_scipy(finder, module):
    finder.IncludePackage("scipy._lib")
    finder.IncludePackage("scipy.misc")
    finder.IncludePackage("scipy.sparse.csgraph._validation")
    finder.IncludePackage("scipy.sparse._csparsetools")
    finder.IncludePackage("scipy.special._ufuncs_cxx")
    finder.IncludePackage("scipy.special.specfun")

hooks.load_scipy = load_scipy

# Trimesh data files
trimesh_resources_path = os.path.join(os.path.dirname(trimesh.__file__), "resources")
trimesh_resources_required_files = [
    "blender.py.template",
    "collada.dae.template",
    "dxf.json.template",
    "ply.template",
    "svg.xml.template",
    "units_to_inches.json",
    "viewer.html.template",
    "yafaray.xml.template",
]
for file_name in trimesh_resources_required_files:
    item = (os.path.join(trimesh_resources_path, file_name), os.path.join("trimesh", "resources", file_name))
    zip_includes.append(item)

def load_pyqt5_qtquick(finder, module):
    finder.IncludeModule("PyQt5.QtCore")
    finder.IncludeModule("PyQt5.QtGui")
    finder.IncludeModule("PyQt5.QtQml")
    finder.IncludeModule("PyQt5.QtNetwork")
    finder.IncludeModule("PyQt5.QtWebSockets")
    finder.IncludeModule("PyQt5._QOpenGLFunctions_2_0")
    finder.IncludeModule("PyQt5._QOpenGLFunctions_2_1")
    finder.IncludeModule("PyQt5._QOpenGLFunctions_4_1_Core")

hooks.load_PyQt5_QtQuick = load_pyqt5_qtquick

def load_pyqt5_qtnetwork(finder, module):
    finder.IncludeModule("PyQt5.QtCore")

    qt_path = os.path.join(os.path.dirname(PyQt5.QtCore.__file__), "Qt", "bin")
    required_ssl_files = [
        "libeay32.dll",
        "ssleay32.dll",
    ]
    for file_name in required_ssl_files:
        finder.IncludeFiles(os.path.join(qt_path, file_name), file_name)

hooks.load_PyQt5_QtNetwork = load_pyqt5_qtnetwork

def load_shapely(finder, module):
    finder.IncludeModule("shapely")
    shapely_path = os.path.join(os.path.dirname(shapely.__file__), "DLLs")
    required_dll_files = [
        "geos_c.dll",
    ]
    for file_name in required_dll_files:
        finder.IncludeFiles(os.path.join(shapely_path, file_name), file_name)

hooks.load_shapely = load_shapely

search_path = sys.path.copy()
search_path.insert(1, "D:/cura411/cura-build-4.11.0/build/inst/lib/python3.8/site-packages/")
search_path.insert(2, "/lib/python3.8/site-packages/")

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {
    "build_exe": "package",
    "zip_include_packages": "*",
    "zip_exclude_packages": "certifi",
    "path": search_path,
    "packages": [
        "appdirs",
        "packaging",
        "cryptography",
        "xml.etree",
        "uuid",
        "serial",
        "zeroconf",
        "requests",
        "idna",
        "UM",
        "cura",
        "scipy.spatial",
        "sip",
        "stl",
        "shapely",
        "netifaces",
        "networkx",
        "trimesh",
        "trimesh.resources",
        "Savitar",
        "PyQt5.QtDBus",
        "comtypes",
        "Charon",
        "logging",
        "logging.config",
        "logging.handlers",
    ],
    "include_files": [
        ("D:/cura411/cura-build-4.11.0/build/inst/bin/CuraEngine.exe", ""),
        ("D:/cura411/cura-build-4.11.0/build/inst/lib/cura/plugins", ""),
        ("D:/cura411/cura-build-4.11.0/build/inst/lib/uranium/plugins", ""),
        ("D:/cura411/cura-build-4.11.0/build/inst/lib/python3.8/site-packages/UM/Qt/qml/UM", "qml/UM"),
        ("D:/cura411/cura-build-4.11.0/build/inst/share/cura/resources", "resources"),
        ("D:/cura411/cura-build-4.11.0/build/inst/share/uranium/resources", "resources"),
        ("/bin/openctm.dll", ""), # For opening .CTM files
        ("/lib/site-packages/PyQt5/Qt/bin/concrt140.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/d3dcompiler_47.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/libcrypto-1_1-x64.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/libeay32.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/libEGL.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/libGLESv2.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/libssl-1_1-x64.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/msvcp140.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/msvcp140_1.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/msvcp140_2.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/opengl32sw.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Bluetooth.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Core.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5DBus.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Designer.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Gui.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Help.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Location.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Multimedia.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5MultimediaWidgets.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Network.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5NetworkAuth.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Nfc.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5OpenGL.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Positioning.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5PositioningQuick.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5PrintSupport.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Qml.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5QmlModels.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5QmlWorkerScript.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Quick.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Quick3D.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Quick3DAssetImport.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Quick3DRender.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Quick3DRuntimeRender.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Quick3DUtils.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5QuickControls2.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5QuickParticles.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5QuickShapes.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5QuickTemplates2.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5QuickTest.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5QuickWidgets.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5RemoteObjects.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Sensors.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5SerialPort.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Sql.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Svg.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Test.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5WebChannel.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5WebSockets.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Widgets.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5WinExtras.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5Xml.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/Qt5XmlPatterns.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/ssleay32.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/vcruntime140.dll",""),
        ("/lib/site-packages/PyQt5/Qt/bin/vcruntime140_1.dll",""),
        # Preinstalled PyQt5 installation
        (PyQt5.__path__[0] + "/Qt/qml/Qt", "qml/Qt"),
        (PyQt5.__path__[0] + "/Qt/qml/QtQml", "qml/QtQml"),
        (PyQt5.__path__[0] + "/Qt/qml/QtQuick", "qml/QtQuick"),
        (PyQt5.__path__[0] + "/Qt/qml/QtQuick.2", "qml/QtQuick.2"),
        (PyQt5.__path__[0] + "/Qt/qml/QtGraphicalEffects", "qml/QtGraphicalEffects"),
    ],
    "zip_includes": zip_includes,
    "excludes": [ ],
    "replace_paths": [("*", "")],
}

executables = [
    Executable(script="D:/cura411/cura-build-4.11.0/build/inst/bin/cura_app.py",
               base="Win32GUI",
               targetName = "Cura.exe",
               icon="D:/cura411/cura-build-4.11.0/packaging/cura.ico"
               ),
    Executable(script="D:/cura411/cura-build-4.11.0/build/inst/bin/cura_app.py",
               base="Console",
               targetName = "CuraCLI.exe",
               icon="D:/cura411/cura-build-4.11.0/packaging/cura.ico"
               ),
]

setup(
    name = "FOKOOS Slicer",
    version = "0.0.0",
    description = "FOKOOS Slicer",
    long_description = "FOKOOS Slicer - 3D Printing Software",
    author = "FOKOOS Slicer",
    url = "http://software.ultimaker.com/",
    license = "GNU LESSER GENERAL PUBLIC LICENSE (LGPL)",

    options = {"build_exe": build_options},
    executables = executables
)
