#!/usr/bin/env python3
"""
GPT-Based scRNA-seq Marker Gene Interpreter
Created at: Tsinghua University Generative AI Summer School, July 2025
Author: Rimsha Kanwal

This tool uses GPT-4 API to interpret gene marker lists from single-cell RNA-seq
data and identify cell types in accessible language.
"""

import os
from openai import OpenAI

# System prompt that guides GPT's interpretation
SYSTEM_PROMPT = """You are an expert in single-cell biology and genomics. Your role is to interpret 
gene marker lists and identify cell types in clear, accessible language suitable for non-specialists.

For each gene list provided:
1. Identify the most likely cell type(s)
2. Explain what these genes do in simple terms
3. Describe the biological function of the identified cell type
4. If relevant, mention clinical or disease implications

Keep explanations concise (2-3 sentences per point) and avoid excessive jargon. When using 
technical terms, briefly explain them."""


def interpret_marker_genes(gene_list, api_key=None):
    """
    Interpret a list of marker genes using GPT-4.
    
    Args:
        gene_list (list): List of gene symbols (e.g., ['CD3D', 'CD4', 'IL7R'])
        api_key (str): OpenAI API key. If None, reads from OPENAI_API_KEY env variable
    
    Returns:
        dict: Contains 'cell_type', 'interpretation', and 'raw_response'
    """
    # Initialize OpenAI client
    if api_key is None:
        api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        return {
            'error': 'No API key provided. Set OPENAI_API_KEY environment variable or pass api_key parameter.'
        }
    
    client = OpenAI(api_key=api_key)
    
    # Format gene list for the prompt
    genes_str = ", ".join(gene_list)
    
    user_prompt = f"""Analyze these marker genes from single-cell RNA-seq data:

Genes: {genes_str}

Please provide:
1. Cell Type: [Identify the cell type]
2. Gene Functions: [Explain what each key gene does]
3. Biological Role: [What does this cell type do in the body?]
4. Clinical Relevance: [Any disease or health implications]"""
    
    try:
        # Call GPT-4 API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,  # Lower temperature for more consistent scientific output
            max_tokens=500
        )
        
        interpretation = response.choices[0].message.content
        
        # Parse the response to extract cell type
        cell_type = "Unknown"
        if "Cell Type:" in interpretation:
            lines = interpretation.split('\n')
            for line in lines:
                if line.strip().startswith("1. Cell Type:") or line.strip().startswith("Cell Type:"):
                    cell_type = line.split(':', 1)[1].strip()
                    break
        
        return {
            'genes': gene_list,
            'cell_type': cell_type,
            'interpretation': interpretation,
            'raw_response': response
        }
        
    except Exception as e:
        return {
            'error': f'API call failed: {str(e)}'
        }


def batch_interpret(gene_lists, api_key=None):
    """
    Interpret multiple gene lists at once.
    
    Args:
        gene_lists (list): List of gene lists, e.g., [['CD3D', 'CD4'], ['CD19', 'MS4A1']]
        api_key (str): OpenAI API key
    
    Returns:
        list: List of interpretation dictionaries
    """
    results = []
    for i, genes in enumerate(gene_lists):
        print(f"Processing gene list {i+1}/{len(gene_lists)}...")
        result = interpret_marker_genes(genes, api_key)
        results.append(result)
    return results


def format_output(result):
    """
    Format the interpretation result for display.
    
    Args:
        result (dict): Result from interpret_marker_genes()
    
    Returns:
        str: Formatted string for printing
    """
    if 'error' in result:
        return f"ERROR: {result['error']}"
    
    output = []
    output.append("=" * 70)
    output.append(f"MARKER GENES: {', '.join(result['genes'])}")
    output.append(f"IDENTIFIED CELL TYPE: {result['cell_type']}")
    output.append("=" * 70)
    output.append("\nINTERPRETATION:")
    output.append(result['interpretation'])
    output.append("\n" + "=" * 70)
    
    return "\n".join(output)


# Pre-defined common marker gene sets for testing/demonstration
COMMON_CELL_TYPES = {
    "Helper T cells": ["CD3D", "CD4", "IL7R"],
    "Cytotoxic T cells": ["CD3D", "CD8A", "CD8B"],
    "B cells": ["CD19", "MS4A1", "CD79A"],
    "NK cells": ["NCAM1", "GNLY", "NKG7"],
    "Monocytes": ["CD14", "LYZ", "S100A8"],
    "Dendritic cells": ["FCER1A", "CD1C", "CLEC10A"],
    "Macrophages": ["CD68", "CD163", "MSR1"],
    "Plasma cells": ["MZB1", "SDC1", "JCHAIN"]
}


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="GPT-powered scRNA-seq marker gene interpreter"
    )
    parser.add_argument(
        '--genes', 
        nargs='+', 
        help='Space-separated list of gene symbols (e.g., CD3D CD4 IL7R)'
    )
    parser.add_argument(
        '--demo', 
        action='store_true',
        help='Run demonstration with common cell type markers'
    )
    parser.add_argument(
        '--api-key',
        help='OpenAI API key (or set OPENAI_API_KEY environment variable)'
    )
    
    args = parser.parse_args()
    
    if args.demo:
        print("\n" + "=" * 70)
        print("DEMONSTRATION MODE: Analyzing Common Cell Type Markers")
        print("=" * 70 + "\n")
        
        # Demo mode - analyze a few example cell types
        demo_cells = ["Helper T cells", "B cells", "NK cells"]
        
        for cell_name in demo_cells:
            genes = COMMON_CELL_TYPES[cell_name]
            print(f"\n[Demo] Analyzing {cell_name} markers: {', '.join(genes)}")
            print("Note: This would call GPT-4 API. Set OPENAI_API_KEY to run actual analysis.")
            print(f"Expected identification: {cell_name}\n")
            
    elif args.genes:
        result = interpret_marker_genes(args.genes, args.api_key)
        print(format_output(result))
        
    else:
        print("Usage:")
        print("  python marker_interpreter.py --genes CD3D CD4 IL7R")
        print("  python marker_interpreter.py --demo")
        print("\nSet OPENAI_API_KEY environment variable before running.")
