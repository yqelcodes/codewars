def my_languages(results):
    newlang = []
    for key in results.keys():
        if results[key] >= 60:
            newlang.append({ "Key": key, "Value": results[key]})
    newlang.sort(key=lambda x: x["Value"], reverse=True)
    return [l["Key"] for l in newlang]