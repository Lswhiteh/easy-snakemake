# easy-snakemake
Quick tutorial and example code for using Snakemake in a non-NGS context.

### Installation
Everything you need to run all the code in this repo is packaged in a conda env. To create and activate it:
```
conda create -f easy-snakemake.yaml
conda activate easy-snakemake
```
 ---

### Simplest Example

This version (in the `simplest` dir) is the most barebones Snakefile you can possibly make. It is essentially equivalent to a GNU Makefile, with the exception of some native Python code running within a rule to show off how you can mix bash and python code in the same Snakefile.

To run it, simply `cd simplest` and then run `snakemake -c 1`. The `-c 1` flag tells Snakemake how many cores to use, which will become much more relevant when scaling up local processes, but for this example one is plenty.

A couple things will happen:
- Snakemake will tell you it's `Building a DAG of jobs...`, which means just that: the workflow manager engine under the hood of Snakemake is going through all the rules defined in the Snakefile, looking at how the files for inputs/outputs flow between processes, and creating an organized "flowchart" of what order things need to be run in to fill the given dependencies. You can visualize this DAG with `snakemake -c 1 --dag | dot -Tpng > dag.png`, which is especially useful for more complex workflows where files can go to multiple inputs/outputs and the dependencies between processes becomes more complex.
- It will then print out a table of jobs, how many times each job will be run, and the threads taken by each. This is handy when you're resuming a run of something that failed previously, it's a quick tell-tale sign that only the processes that need to run are doing so.
- Finally, Snakemake will start logging the rules as it runs them. The format is straightforward, with the date-time, rule name, input/output, job id, and any resources defined logged as the rule is launched. There will also be logs of when a job finishes, and how much of the total number of jobs are complete for the entire workflow.
- After Snakemake closes, you'll notice the input to the `all` rule, `Confusion_matrix.png` (and all the intermediate npzs) is saved to disk and viewable. 




---

### TODO
- dryruns
- glob_wildcards
- clean rule