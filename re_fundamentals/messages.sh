#!/bin/bash

SCRIPT_DIR="$(dirname "$0")"
source "$SCRIPT_DIR/messages.sh"

if [ $# -ne 1 ]; then
    echo "İstifadə qaydası: $0 <elf_fayl>"
    exit 1
fi

file_name="$1"

if [ ! -f "$file_name" ]; then
    echo "Xəta: '$file_name' faylı tapılmadı."
    exit 1
fi

if ! readelf -h "$file_name" > /dev/null 2>&1; then
    echo "Xəta: '$file_name' etibarlı ELF faylı deyil."
    exit 1
fi

magic_number=$(readelf -h "$file_name" | grep "Magic" | sed 's/Magic:\s*//')
class=$(readelf -h "$file_name" | grep "Class:" | awk '{print $2}')
byte_order=$(readelf -h "$file_name" | grep "Data:" | sed 's/.*Data:\s*//')
entry_point_address=$(readelf -h "$file_name" | grep "Entry point address:" | awk '{print $NF}')

display_elf_header_info
