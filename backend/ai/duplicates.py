def merge_duplicates(reports):
    merged = []
    seen = set()
    for r in reports:
        key = (r['lat'], r['lon'], r['category'])
        if key in seen:
            for m in merged:
                if (m['lat'], m['lon'], m['category']) == key:
                    m['merged_count'] += 1
        else:
            r['merged_count'] = 1
            merged.append(r)
            seen.add(key)
    return merged
