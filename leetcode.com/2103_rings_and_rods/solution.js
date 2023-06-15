var countPoints = function(rings) {
    let rods = new Map();

    for (let i = 0 ; i < rings.length - 1 ; i += 2) {
        switch (rings[i]) {
            case 'R':
                rods.set(rings[i + 1], rods.get(rings[i + 1]) | (1 << 0));
                break;
            case 'G':
                rods.set(rings[i + 1], rods.get(rings[i + 1]) | (1 << 1));
                break;
            case 'B':
                rods.set(rings[i + 1], rods.get(rings[i + 1]) | (1 << 2));
                break;
        }
    }

    let total = 0;

    for (let v of rods.values()) {
      if (v == (1 | 2 | 4))
          total++;
    }

    return total;
};
