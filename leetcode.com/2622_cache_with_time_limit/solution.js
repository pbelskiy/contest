
var TimeLimitedCache = function() {
    this.d = {};
    this.t = {};
};

TimeLimitedCache.prototype.set = function(key, value, duration) {
    let result = false;

    if (String(key) in this.d) {
        clearTimeout(this.t[key]);
        result = true;
    }

    this.d[key] = value;
    this.t[key] = setTimeout(function(d) {
        delete d[key];
    }, duration, this.d);

    return result;
};

TimeLimitedCache.prototype.get = function(key) {
    if (String(key) in this.d)
        return this.d[key];

    return -1;
};

TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.d).length;
};
