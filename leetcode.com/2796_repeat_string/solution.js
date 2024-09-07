String.prototype.replicate = function(times) {
    s = ''

    for (i = 0 ; i < times ; i++)
        s += this

    return s
}
