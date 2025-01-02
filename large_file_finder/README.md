# Large File Finder
A simple script that allows you to size up all the files and folders within a given directory, returning the top 10 largest folders/files and allowing you to open parent directories to delete large files.

```
run large_file_finder.py [path] [num_results]
```

The script defaults to the Library folder as the path and 10 results as num_results.

To adjust the path and num_results:

```
run large_file_finder.py <some/path> --num_results <some_integer>
```

### Example Output:

```
>>> run large_file_finder.py

>>> TOP 10 FOLDERS BY SIZE IN /USERS/<USER>/LIBRARY
/Users/<USER>/Library/Application Support: 11095.01 MB
   Steam: 4902.30 MB
   Arc: 1798.33 MB
   Google: 1706.32 MB
   Code: 872.27 MB
   discord: 490.68 MB
   Notion: 367.55 MB
   Caches: 258.23 MB
   CloudDocs: 245.72 MB
   OpenEmu: 156.73 MB
   AddressBook: 60.90 MB
/Users/<USER>/Library/Caches: 10559.01 MB
   company.thebrowser.Browser: 4847.06 MB
   pip: 2173.68 MB
   Arc: 1351.00 MB
   com.spotify.client: 609.09 MB
   Google: 500.77 MB
   loom-updater: 176.95 MB
   CloudKit: 173.10 MB
   com.grammarly.ProjectLlama: 144.43 MB
   com.linguee.DeepLCopyTranslator: 104.86 MB
   Homebrew: 73.94 MB
/Users/<USER>/Library/Developer: 3254.10 MB
   CoreSimulator: 1784.69 MB
   Xcode: 1456.68 MB
/Users/<USER>/Library/Metadata: 1925.72 MB
   CoreSpotlight: 1925.44 MB
/Users/<USER>/Library/Photos: 1753.74 MB
   Libraries: 1753.74 MB
/Users/<USER>/Library/Containers: 1664.52 MB
   com.tinyspeck.slackmacgap: 807.45 MB
   com.apple.BKAgentService: 189.96 MB
   com.apple.geod: 109.92 MB
   com.apple.photoanalysisd: 96.60 MB
   com.apple.mediaanalysisd: 86.59 MB
   com.apple.Maps: 70.65 MB
   com.docker.docker: 57.60 MB
   com.endel.endel: 52.20 MB
   com.apple.iBooksX: 47.12 MB
   com.apple.mail: 24.08 MB
/Users/<USER>/Library/Messages: 1620.13 MB
   Caches: 601.49 MB
   Attachments: 43.30 MB
   StickerCache: 1.90 MB
   Drafts: 0.00 MB
/Users/<USER>/Library/Mail: 1369.99 MB
   V10: 1369.98 MB
/Users/<USER>/Library/Arduino15: 948.26 MB
   packages: 717.26 MB
   staging: 193.67 MB
   libraries: 2.40 MB
/Users/<USER>/Library/Mobile Documents: 576.48 MB
   iCloud~com~apple~Playgrounds: 274.42 MB
   com~apple~CloudDocs: 227.80 MB
   iCloud~com~apple~iBooks: 27.13 MB
   57T9237FN3~net~whatsapp~WhatsApp: 19.54 MB
   com~apple~Keynote: 14.66 MB
   com~apple~Pages: 6.56 MB
   com~apple~shoebox: 1.36 MB
   iCloud~com~streaksapp~streak: 0.77 MB
   iCloud~com~PlausibleConcept~BadNorth: 0.55 MB
   iCloud~com~ustwo~monumentvalley2: 0.45 MB
TOP 10 SUB-FOLDERS BY SIZE
Steam: 4902.30 MB
company.thebrowser.Browser: 4847.06 MB
pip: 2173.68 MB
CoreSpotlight: 1925.44 MB
CoreSimulator: 1784.69 MB
Libraries: 1753.74 MB
Google: 1706.32 MB
Xcode: 1456.68 MB
V10: 1369.98 MB
Arc: 1351.00 MB
TOP 10 FILES BY SIZE
/Users/<USER>/Library/Developer/CoreSimulator/Caches/dyld/23G93/com.apple.CoreSimulator.
SimRuntime.watchOS-9-4.20T253/dyld_sim_shared_cache_arm64: 1610.25 MB
/Users/<USER>/Library/Application Support/Steam/steamapps/common/Caves of
Qud/CoQ.app/Contents/Resources/Data/resources.resource: 733.37 MB
/Users/<USER>/Library/Photos/Libraries/Syndication.photoslibrary/database/Photos.sqlite:
707.35 MB
/Users/<USER>/Library/Application Support/Steam/steamapps/common/Arco Demo/arco.exe:
622.01 MB
/Users/<USER>/Library/Application Support/Steam/steamapps/common/Arco
Demo/Arco.app/Contents/Resources/Arco.love: 621.99 MB
/Users/<USER>/Library/Messages/chat.db: 602.34 MB
/Users/<USER>/Library/Caches/company.thebrowser.Browser/org.sparkle-project.Sparkle/Inst
allation/QBuPYV1S9/Arc.app/Contents/Frameworks/ArcCore.framework/Versions/A/ArcCore: 389.96
MB
/Users/<USER>/Library/Caches/company.thebrowser.Browser/org.sparkle-project.Sparkle/Inst
allation/qswttjirc/Arc.app/Contents/Frameworks/ArcCore.framework/Versions/A/ArcCore: 386.91
MB
/Users/<USER>/Library/Caches/company.thebrowser.Browser/org.sparkle-project.Sparkle/Inst
allation/1Fj1lRst3/Arc.app/Contents/Frameworks/ArcCore.framework/Versions/A/ArcCore: 382.11
MB
/Users/<USER>/Library/Caches/company.thebrowser.Browser/org.sparkle-project.Sparkle/Inst
allation/yzqMWQYrn/Arc.app/Contents/Frameworks/ArcCore.framework/Versions/A/ArcCore: 382.10
MB

Sized up all the folders and files in /Users/<USER>/Library.
Would you like to open the folders for the largest files?
 [y/N]:
```

### Features in Progress:
- attempting to implement the script into a GUI for a better UX by leveraging Textual and Rich
