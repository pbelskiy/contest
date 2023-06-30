class EventEmitter {

    constructor() {
        this.list = {};
    }

    subscribe(event, cb) {
        if (event in this.list) {
            this.list[event].push(cb);
        } else {
            this.list[event] = [cb];
        }

        return {
            unsubscribe: () => {
                for (let i = 0 ; i < this.list[event].length ; i++) {
                    if (this.list[event][i] == cb) {
                        this.list[event].splice(i, 1);
                        return;
                    }
                }
            }
        };

    }

    emit(event, args = []) {
        let result = [];

        if (this.list[event] === undefined)
            return result;

        for (let i = 0 ; i < this.list[event].length ; i++) {
            result.push(this.list[event][i](...args));
        }

        return result;
    }
}
