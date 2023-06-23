var addTwoPromises = async function(promise1, promise2) {
    let r1 = await promise1;
    let r2 = await promise2;

    return r1 + r2;
};
