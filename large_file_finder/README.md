# Large File Finder
A simple script that allows you to size up all the files and folders within a given directory, returning the top 10 largest folders/files and allowing you to open parent directories to delete large files.

```
run large_file_finder.py [path] [num_results]
```

The script defaults to the Library folder as the path and 10 results as num_results.

To adjust the path and the num_results:

```
run large_file_finder.py <some/path> --num_results <some_integer>
```

### Features in Progress
- attempting to implement the script into a GUI for a better UX by leveraging Textual and Rich
