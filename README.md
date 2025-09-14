# Approximating Signed Distance Fields of Implicit Surfaces with Sparse Ellipsoidal Radial Basis Function Networks
![Overview](doc/overview.png)

---

## Instructions for SE-RBFNet (under Linux): 

### 1. Clone the Repository

```bash
git clone https://github.com/lianbobo/SE-RBFNet.git
cd SE-RBFNet
```
#### This repository includes the following folders:

- app/      : Contains executable `.so` files for OCtree construction  and reconstruction. OCtree-related components are adapted from https://github.com/jsnln/ParametricGaussRecon.git

- DATA/     : Includes several sample point cloud datasets. Full benchmark data can be found at https://github.com/ErlerPhilipp/points2surf.git

- results/  : Output directory for sampled point clouds, OCtree data, reconstructed surfaces, etc.


### 2. Environment Setup
Before running the main program, install the required Python packages:
```
pip install -r requirements.txt
```
Tested Environment: Python 3.10, CUDA 12.1, Ubuntu 18.04


### 3. Execute main.py. 
- file: Path to the input mesh file (e.g., 'DATA/Armadillo.ply')

- sample_num: Number of points to sample from the mesh (e.g., 40000)

- batch_size: batch size (e.g., 10000)

- thres_min: threshold (e.g., 0.02)

- save_path: Directory to store the output results (e.g., 'results')

- seed: Random seed for reproducibility (e.g., 0)


### 4. Output
Once the script finishes, all results (sampled point clouds, OCtree data, reconstructed surfaces) will be saved under the results/ directory.






------------------------------------------------------------------------------------------------------------------------
#### Contact
If you encounter any issues running this project, feel free to contact: \
Dr. Bobo Lian \
email: 20244007006@stu.suda.edu.cn
   
