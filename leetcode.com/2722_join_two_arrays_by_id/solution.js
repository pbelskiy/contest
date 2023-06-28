var join = function(arr1, arr2) {
    let merged = {};

    for (let i = 0 ; i < arr1.length ; i++) {
        merged[arr1[i].id] = arr1[i];
    }

    for (let i = 0 ; i < arr2.length ; i++) {
        if (!(arr2[i].id in merged)) {
            merged[arr2[i].id] = arr2[i];
            continue;
        }

        merged[arr2[i].id] = Object.assign(merged[arr2[i].id], arr2[i]);
    }

    let result = [];
    let keys = Object.keys(merged).map(k => +k);

    for (let i = 0 ; i < keys.length ; i++) {
        result.push(merged[keys[i]]);
    }

    return result;
};
