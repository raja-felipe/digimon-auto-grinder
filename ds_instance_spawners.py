import multiprocessing
import subprocess

def run_instance(instance_id):
    # Replace with the command to run your script
    subprocess.run(['python', 'src/ds_runner.py', str(instance_id)])

if __name__ == "__main__":
    num_instances = 40
    processes = []

    for i in range(num_instances):
        p = multiprocessing.Process(target=run_instance, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()