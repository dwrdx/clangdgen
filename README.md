# clangdgen
A simple utility to generate compile_commands.json for clangd

[clangd](https://clangd.llvm.org/) is a really great tool to help you to navigate 
through C/C++ source code, however It requires compile_commands.json file to help clangd tool to understand your C/C++ project. Generating compile_commands.json based on the methods that documented in the offical documents sometime is way too complex.

This small script is to help you to generate compile_commands.json a little bit easier.  It simply walks through all your folders in your huge C/C++ project put all source files and all header filders in compile_commands.json file. 

The generated file by this script may not accurate enough to describe every defines/macros in your project becasue all the information does not come from a build system, but It's fairly easy to use. 

Sometimes, we just want something simple and easy.


## Dependencies
* [click](https://click.palletsprojects.com/en/8.0.x/)
* [clangd](https://clangd.llvm.org/installation)