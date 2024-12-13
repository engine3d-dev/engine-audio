from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.scm import Git
from conan.tools.files import copy
import os

class AudioRecipe(ConanFile):
    name = "engine3d-audio"
    version = "1.0"
    package_type = "library"
    license = "Apache-2.0"
    homepage = "https://github.com/engine3d-dev/engine3d-audio"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = "CMakeLists.txt", "src/CMakeLists.txt", "demo/CMakeLists.txt", "engine3d-audio/*.h", "engine3d-audio/internal/*.h", "src/engine3d-audio*", "demo/*", "engine3d-audio/Sound.hpp"

    def build_requirements(self):
        self.requires("make/4.4.1")
        self.tool_requires("cmake/3.27.1")

    def layout(self):
        cmake_layout(self)
    
    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        tc = CMakeToolchain(self, generator="Unix Makefiles")
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        cmake.build()
    
    def package(self):
        copy(self, "LICENSE", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        copy(self, pattern="*.h", src=os.path.join(self.source_folder, "engine3d-audio"), dst=os.path.join(self.package_folder, "engine3d-audio"))
        copy(self, pattern="*.hpp", src=os.path.join(self.source_folder, "engine3d-audio"), dst=os.path.join(self.package_folder, "engine3d-audio"))
        copy(self, pattern="*.h", src=os.path.join(self.source_folder, "engine3d-audio/internal"), dst=os.path.join(self.package_folder, "engine3d-audio/internal"))
        copy(self, pattern="*.a", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, pattern="*.so", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, pattern="*.lib", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, pattern="*.dll", src=self.build_folder, dst=os.path.join(self.package_folder, "bin"), keep_path=False)
        copy(self, pattern="*.dylib", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_target_name", "engine3d-audio::engine3d-audio")
        self.cpp_info.libs = ["engine3d-audio"]
        self.cpp_info.includedirs = ['./', './engine3d-audio']
