# A small script to generate clangd compile_commands.json
# By Edward XU
import os
import json

try:
    import click
except:
    print("Library click is required by this script")


@click.command()
@click.option('--src', required=True, help='path of source code to generate clangd configuration.')
@click.option('--clangd', required=True, help='path to keep clangd configuration.')
@click.option('--defines', required=False, help='opiontal added more defines')
def main(src, clangd, defines):
    database = []

    include_folders = []
    if os.path.isdir(src):
        if os.path.isdir(clangd):
            for p in os.walk(src):
                found = False
                for file in p[2]:
                    if file.endswith('.c') or file.endswith('.h'):
                        found = True
                        break
                if found:
                    if p[0] not in include_folders:
                        include_folders.append(p[0])
            
            include_string = ' '.join([f'\"-I{d}\"' for d in include_folders])

            if defines:
                include_string = ' '.join([include_string, f'\"{defines}\"'])

            for root, _, files in os.walk(src):
                for file in files:
                    if file.endswith('.c'):
                        compile_entry = {}
                        compile_entry['directory'] = os.path.abspath(os.path.curdir)
                        compile_entry['command'] = f'gcc {include_string} \
                                                     -o {file}.o -c {os.path.join(root, file)}'
                        compile_entry['file'] = os.path.join(root, file)
                        database.append(compile_entry)

            with open(os.path.join(clangd, 'compile_commands.json'), 'w') as f:
                json.dump(database, f, indent=4)

        else:
            print(clangd + " is not a valid folder to put clangd config file")
    else:
        print(src + " is not a valid folder for source code")

if __name__ == '__main__':
    main()
