# Change to /tmp directory
os.chdir('/tmp')

# Copy models directory
subprocess.run(['cp', '-r', '/eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/test/RecoEgamma-EgammaPhotonProducers/models', './'])
os.chdir('/tmp/models/')
#subprocess.run('ls -ltrh')
os.chdir('/eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/')
# Custom function to simulate Triton server and run jobs
def run_job():
    # 1. Start the Triton server (if required)
    triton_command = [
        "singularity", "exec", "--nv", "/cvmfs/unpacked.cern.ch/registry.hub.docker.com/fastml/triton-torchgeo:22.07-py3-geometric",
        "tritonserver", "--model-repository", "/tmp/models", "--http-port", "8000", "--grpc-port", "8001", "--metrics-port", "8002", "--allow-http=1"
    ]
#    triton_process = subprocess.Popen(triton_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)  # Give it some time to start
    subprocess.run("ps aux | grep triton", shell=True, check=True)

    # 2. Loop through the input files and process them with cmsRun
    counter = 1
    max_count = 2
    input_list = 'input_files.txt'

    with open(input_list, 'r') as f:
        for input_file in f:
            input_file = input_file.strip()
            if not input_file or input_file.startswith("#"):
                continue

            output_file = f"NTuple_{counter:03d}.root"
            print(f"Processing input: {input_file}")
            print(f"Output will be: {output_file}")

            # Run cmsRun with the inputFile argument
            os.environ['CMSSW_BASE'] = '/eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src'  # Set up environment if needed
            os.chdir('/eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/test')
            subprocess.run(['cmsRun', 'Zee_dumper_MINIAOD_MC_cfg_copy.py', f'inputFile={input_file}'])

            # Change to the next directory and run the next cmsRun
            os.chdir('/eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/EM_Skimmer/ZeeAnalyzer/test')
            subprocess.run(['cmsRun', 'Electron_RecHit_AODSIM_cfg_mod.py'])

            # Move the result and rename output
            os.rename('ElectronRecHits_Ntuple.root', output_file)
            shutil.move(output_file, f'/eos/user/b/bbapi/Energy_regression/CMSSW_13_3_3/src/EM_Skimmer/ZeeAnalyzer/test/Data/{output_file}')

            # Stop iteration if we reach the max count
            if counter == max_count:
                break
            counter += 1

    # Terminate the Triton server once done
    triton_process.terminate()
    triton_process.wait()

# Run the job
run_job()
