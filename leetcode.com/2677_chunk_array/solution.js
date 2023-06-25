var chunk = function(arr, size) {
    let chunks = [];
    let last = [];

    for (let i = 0 ; i < arr.length ; i++) {
        last.push(arr[i]);

        if (last.length == size) {
            chunks.push(last);
            last = [];
        }
    }

    if (last.length > 0)
        chunks.push(last);

    return chunks;
};
