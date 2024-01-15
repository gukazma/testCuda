from conans import ConanFile, tools
import platform


class ModuleConan(ConanFile):
    name = "QtConanExample"
    description = "An example for Qt with Conan"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package_multi", "cmake_paths"

    def configure(self):
        del self.settings.compiler.cppstd

    def requirements(self):
        self.requires("gtest/1.14.0")
        
    def imports(self):
        self.copy("*.dll", "./bin", "bin")
        self.copy("*.so", "./bin", "bin")
