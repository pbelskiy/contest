var flat = function (arr, n) {
    let res = [];

    function solve(a, n) {
        for (let i = 0 ; i < a.length ; i++) {
            if (typeof a[i] === 'object' && n > 0) {
                solve(a[i], n - 1);
            } else {
                res.push(a[i]);
            }
        }
    }

    solve(arr, n)
    return res;
};
