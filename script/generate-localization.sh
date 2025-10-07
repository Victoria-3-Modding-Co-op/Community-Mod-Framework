#!/bin/bash

if [ -e "$1" ]
then
  baseLanguage='english'
else
  baseLanguage="$1"
fi

echo "Generating new localization files from $baseLanguage as a base"
echo ' '

while read -r language; do
  if [ -d "$2localization/$language/" ]
  then
  echo "Removing old folder for $language language"
    rm -r "$2localization/$language/"
  fi
  echo "Creating folder for $language language"
  cp -R "$2localization/$baseLanguage/" "$2localization/$language/"
  while IFS= read -r filename ; do
      [ -f "$2$filename" ] || continue
      sed -i "s/l_$baseLanguage/l_$language/g" "$2$filename"
      mv "$2$filename" "$2${filename//l_$baseLanguage/l_$language}"
  done < <(find "$2." -wholename "*localization/$language/*.yml" -type f -printf "%P\n")
done < languages.txt