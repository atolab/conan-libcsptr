#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class LibcsptrConan(ConanFile):
    name = "libcsptr"
    version = "2.0.4"
    description = "Smart pointers for the (GNU) C programming language"
    url = "https://github.com/k0ekk0ek/conan-libcsptr"
    homepage = "https://github.com/Snaipe/libcsptr"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "tests": [True, False],
        "sentinel": [True, False],
        "fixed_allocator": [True, False],
        "coveralls": [True, False],
        "coveralls_upload": [True, False]
    }
    default_options = (
        "shared=False",
        "fPIC=True",
        "tests=False",
        "sentinel=True",
        "fixed_allocator=False",
        "coveralls=False",
        "coveralls_upload=True"
    )

    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def source(self):
        source_url = "https://github.com/Snaipe/libcsptr"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["TESTS"] = self.options.tests
        cmake.definitions["SENTINEL"] = self.options.sentinel
        cmake.definitions["FIXED_ALLOCATOR"] = self.options.fixed_allocator
        cmake.definitions["COVERALLS"] = self.options.coveralls
        cmake.definitions["COVERALLS_UPLOAD"] = self.options.coveralls_upload
        if self.settings.os != 'Windows':
            cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.fPIC
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
