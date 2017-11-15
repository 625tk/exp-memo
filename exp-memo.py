import argparse
import os
import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', action='store', nargs=1, type=str)
    parser.add_argument('-o', '--output_dir', action='store', nargs=1, type=str)
    parser.add_argument('-c', '--comment', action='store', nargs=1, type=str)

    args = parser.parse_args()
    if not os.path.exists(args.output_dir[0]):
        readme_path = os.path.join(args.output_dir[0], "README")
        os.makedirs(args.output_dir[0])
        with open(readme_path, mode="w") as f:
            f.write(f"created by {__file__}\n")
            f.write(f"query {args.query[0]}\n")
            f.write(f"comment: {args.comment[0]}\n")
        exec_log_path = os.path.join(args.output_dir[0], "exec.log")
        print(exec_log_path)
        query = f"/usr/bin/time -v -o {exec_log_path} " + args.query[0]

        result = subprocess.run(query, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout_path = os.path.join(args.output_dir[0], "stdout.log")

        with open(stdout_path, mode="w") as f:
            f.write(result.stdout.decode())
        stderr_path = os.path.join(args.output_dir[0], "stderr.log")
        with open(stderr_path, mode="w") as f:
            f.write(result.stderr.decode())
    else:
        print("file aleady exists!")

