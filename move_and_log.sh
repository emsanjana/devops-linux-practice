#!/bin/bash

DIR_NAME="backup_folder"
FILE_NAME="test_file.txt"

if [ ! -f "$FILE_NAME" ]; then
    echo "This is a test file" > "$FILE_NAME"
    echo "$(date): Created $FILE_NAME" >> script.log
fi

mkdir -p "$DIR_NAME"
echo "$(date): Created folder $DIR_NAME" >> script.log

mv "$FILE_NAME" "$DIR_NAME/"
echo "$(date): Moved $FILE_NAME to $DIR_NAME" >> script.log

cat script.log

