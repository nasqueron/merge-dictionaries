# Merge dictionaries

## Root problem

You uses everal IDEs and each maintain its own spelling dictionary.

You want to merge them so words from PyCharm are available in PhpStorm too.

## Usage

### Merge all dictionaries

To discover dictionaries in your computer, extract words and merge them:

```shell
$ merge-dictionaries --merge
```

This is a potentially destructive operation:
your dictionary files will be overwritten.

### Extract dictionaries words

To print all the words:

```shell
$ merge-dictionaries --extract
```

This is a safe operation.

### Build an Hunspell-compatible dictionary

To create a personal dictionary file for your Hunspell dictionary:

```shell
$ merge-dictionaries --extract > perso.dic
```

This is a safe read-only operation,
as long as perso.dic doesn't already exist in your current folder.

### Build a dictionary in a IDE specific format

You can specify `--format=<format>` as argument to the extract task:

```shell
$ merge-dictionaries --extract --format=JetBrains
```

It will output a dictionary file you can use in any IDE compatible with that format.

This is a safe read-only operation.

## IDE support

Currently, the following IDEs are supported

* All JetBrains IDEs: application-level dictionary

## Extend the code
### How to add an IDE?

To add an IDE, you need to provide the following methods:

* sources
  * a list of paths candidates for the IDE dictionary
  * a method extracting words from the dictionary
* output
  * a method to dump the extracted words in the IDE format
* write
  * a method to save the files, normally you can call the ones created

### How can I contribute?

You can commit your changes to the upstream by following instructions at https://agora.nasqueron.org/How_to_contribute_code

The canonical repository is https://devcentral.nasqueron.org/source/merge-dictionaries.git

## License

BSD-2-Clause, see [LICENSE](LICENSE) file.
