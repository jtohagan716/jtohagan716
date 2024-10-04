import shutil

def write_disk_usage_to_file(file_path):
    # Get disk usage statistics
    total, used, free = shutil.disk_usage("/")
    
    # Prepare the output
    output = (
        f"Total Disk Space: {total // (2**30)} GiB\n"
        f"Used Disk Space: {used // (2**30)} GiB\n"
        f"Free Disk Space: {free // (2**30)} GiB\n"
    )
    
    # Write to the specified file
    with open(file_path, 'w') as file:
        file.write(output)

if __name__ == "__main__":
    # Specify the path to the output file
    output_file = "disk_usage.txt"
    write_disk_usage_to_file(output_file)
    print(f"Disk usage written to {output_file}")
