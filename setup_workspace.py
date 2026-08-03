import os

# Define the master folder name
BASE_DIR = "python_mastery"

# Complete curriculum structure mapped from your milestone roadmap
STRUCTURE = {
    "Phase_1_Core_Python": {
        "m01_collections_mastery": ["employee_grouper.py", "duplicate_prompts.py", "dict_merger.py", "word_frequency.py", "flatten_list.py", "remove_dup_dicts.py", "top_k_frequent.py", "pivot_json.py"],
        "m02_functions": ["dynamic_filtering.py", "generic_transformer.py", "data_validation.py", "config_parser.py"],
        "m03_file_processing": ["process_5gb_jsonl.py", "count_labels.py", "merge_logs.py", "read_chunkwise.py", "lazy_loading.py", "csv_aggregation.py"],
        "m04_exception_handling": ["retry_api.py", "skip_bad_records.py", "continue_processing.py", "error_report.py"],
        "m05_oop_design": ["embedding_provider.py", "vector_db.py", "prompt_builder.py", "llm_provider.py", "agent.py"],
        "m06_iterators_generators": ["large_dataset.py", "streaming_embeddings.py", "streaming_logs.py", "infinite_generators.py", "batch_generator.py"],
        "m07_decorators": ["retry_decorator.py", "timer_decorator.py", "logging_decorator.py", "cache_decorator.py", "auth_decorator.py"],
        "m08_collections_library": ["lru_cache.py", "sliding_window.py", "frequency_counter.py", "queue_simulation.py"],
        "m09_itertools": ["cartesian_products.py", "permutations.py", "combinations.py", "grouping.py", "batching.py"],
        "m10_functools": ["partial_functions.py", "lru_cache_mod.py", "reduce_mod.py", "custom_sorting.py"]
    },
    "Phase_2_DS_Interviews": {
        "m11_feature_engineering": ["missing_values.py", "normalization.py", "categorical_encoding.py", "aggregation.py", "window_features.py"],
        "m12_time_series": ["rolling_average.py", "moving_windows.py", "sessionization.py", "gap_detection.py"],
        "m13_evaluation_metrics": ["precision_recall.py", "f1_roc_matrix.py"],
        "m14_data_cleaning": ["dup_removal.py", "outlier_detection.py", "messy_json_parser.py", "column_transforms.py"],
        "m15_sql_without_pandas": ["group_by.py", "join.py", "having.py", "aggregation.py"],
        "m16_memory_optimization": ["generators_yield.py", "chunk_processing.py", "streaming.py"],
        "m17_pandas_scenarios": ["pandas_cleaning.py", "pandas_grouping.py", "pandas_window.py", "pandas_merge.py", "pandas_explode_pivot.py"],
        "m18_numpy_scenarios": ["vectorization.py", "broadcasting.py", "masking.py"],
        "m19_visualization": ["quick_eda.py", "simple_plots.py"],
        "m20_mini_ds_project": ["end_to_end_pipeline.py"]
    },
    "Phase_3_GenAI_Coding": {
        "m21_chunking": ["recursive_chunking.py", "overlap.py", "sentence_chunking.py"],
        "m22_embedding_pipeline": ["batch_embeddings.py", "caching.py", "parallel_embeddings.py"],
        "m23_vector_search": ["cosine_similarity.py", "top_k_retrieval.py", "metadata_filtering.py"],
        "m24_prompt_builder": ["prompt_templates.py", "variable_injection.py", "safety_filters.py"],
        "m25_llm_retry_framework": ["retry_backoff.py", "timeout.py", "circuit_breaker.py"],
        "m26_rag_pipeline": ["rag_workflow.py"],
        "m27_evaluation": ["faithfulness_precision.py", "relevance_latency.py"],
        "m28_async_programming": ["asyncio_semaphore.py", "concurrent_api.py"],
        "m29_threadpool_executor": ["concurrent_embeddings.py", "concurrent_requests.py"],
        "m30_rate_limiter": ["sliding_window.py", "token_bucket.py", "queue_limiter.py"],
        "m31_caching": ["lru_redis_abstraction.py", "ttl_cache.py"],
        "m32_logging": ["structured_logs.py", "trace_ids_timing.py"],
        "m33_agent_framework": ["tool_calling_memory.py", "planning_execution.py"],
        "m34_production_utilities": ["config_loader.py", "secrets_env.py", "yaml_parsing.py"],
        "m35_mini_genai_project": ["complete_rag_implementation.py"]
    },
    "Phase_4_Interview_Practice": {
        "m36_to_50_mock_rounds": ["process_millions.py", "retry_failed_llm.py", "parallel_embedding_service.py", "rate_limiter_design.py", "ai_pipeline_design.py", "evaluate_rag.py", "prompt_optimization.py", "mini_vector_search.py", "caching_layer.py", "llm_abstraction.py"]
    }
}

def create_workspace():
    count_dirs = 0
    count_files = 0
    
    # Generate Directories and Empty Starter Files
    for phase, milestones in STRUCTURE.items():
        for milestone, files in milestones.items():
            dir_path = os.path.join(BASE_DIR, phase, milestone)
            os.makedirs(dir_path, exist_ok=True)
            count_dirs += 1
            
            for file_name in files:
                file_path = os.path.join(dir_path, file_name)
                if not os.path.exists(file_path):
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(f'"""\nMilestone: {milestone}\nTask: {file_name.replace(".py", "").replace("_", " ").title()}\n"""\n\n')
                    count_files += 1
                    
    print(f"🎉 Success! Created {count_dirs} milestone directories and {count_files} starter python files inside '{BASE_DIR}/'.")

if __name__ == "__main__":
    create_workspace()
