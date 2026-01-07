FROM mambaorg/micromamba:1.5.10

USER root

# Create env with tools
RUN micromamba create -y -n scetl -c conda-forge -c bioconda \ 
    python=3.11 \
    fastqc=0.12.* \
    multiqc=1.21 \
    salmon=1.10.* \
    pandas=2.* \
    numpy=1.* \
    scipy=1.* \
    scanpy=1.10.* \
    anndata=0.10.* \
    umap-learn=0.5.* \
    matplotlib \
    scikit-learn \
    boto3=1.* \
    pip \
&& micromamba clean -a -y

ENV PATH=/opt/conda/envs/scetl/bin:$PATH
ENV MAMBA_DOCKERFILE_ACTIVATE=1

WORKDIR /work 

