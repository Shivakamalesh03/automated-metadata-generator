def summarize_text_transformers(text):
    if summarizer is None:
        return "Summary not available (summarizer not loaded)"

    try:
        chunks = [" ".join(text.split()[i:i + 500]) for i in range(0, len(text.split()), 500)]
        summary_chunks = []

        for chunk in chunks[:2]:  # Limit to 2 chunks for speed
            if len(chunk.strip().split()) < 50:
                continue
            result = summarizer(chunk, max_length=130, min_length=40, do_sample=False)
            if result and isinstance(result, list) and len(result) > 0:
                summary = result[0].get("summary_text", "")
                if summary:
                    summary_chunks.append(summary)

        final_summary = " ".join(summary_chunks).strip()

        if final_summary:
            return final_summary
        else:
            logging.warning("Empty result from summarizer, using fallback.")
            return " ".join(text.split()[:60]) + "..."

    except Exception as e:
        logging.warning(f"Summarization failed: {e}")
        fallback = " ".join(text.split()[:60]) + "..."
        return fallback if fallback.strip() else "Summary not available"


