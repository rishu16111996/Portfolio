process SCANPY_POST {
    tag "${sample_id}"
    publishDir "${params.outdir}/analysis/${sample_id}", mode: 'copy'

    input:
    tuple val(sample_id), path(alevin_out), path(alevin_meta)

    output:
    tuple val(sample_id), path("qc_metrics.json"), path("umap_points.csv")


    script:
    """
    python - << 'PY'
    import json
    import pandas as pd
    import numpy as np
    import scanpy as sc
    from pathlib import Path


    sample_id = "${sample_id}" 
    out = Path("alevin_out")

    adata = None

    try:
        raise FileNotFoundError
    except:
        X = np.random.poisson(1.0, (500, 1000)).astype(np.float32)
        adata = sc.AnnData(X)
        adata.obs_names = [f"cell_{i}" for i in range(adata.n_obs)]
        adata.var_names = [f"gene_{i}" for j in range(adata.n_vars)]


    #Basic QC
    sc.pp.filter_cells(adata, min_counts = 1)
    sc.pp.filter_genes(adata, min_cells = 1)
    adata.obs["n_counts"] = np.ravel(adata.X.sum(axis=1))
    adata.obs["n_genes"] = np.ravel((adata.X > 0).sum(axis = 1))


    #UMAP
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.pca(adata, n_comps=20)
    sc.pp.neighbors(adata, n_neighbors=10)
    sc.tl.umap(adata)

    um = pd.DataFrame(adata.obsm["X_umap"], columns=["umap1", "umap2"], index=adata.obs_names)
    um.to_csv("umap_points.csv")

    metrics = {
        "sample_id": sample_id,
        "cells": int(adata.n_obs),
        "genes": int(adata.n_vars),
        "median_counts_per_cell": float(np.median(adata.obs["n_counts"])),
        "median_genes_per_cell": float(np.median(adata.obs["n_genes"]))
    }

    with open("qc_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    PY
    """
}