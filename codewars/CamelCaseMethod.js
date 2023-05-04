String.prototype.camelCase = function () {
    const splitted = this.split(" ");
    const result = splitted.map((word) => {
        return word.charAt(0).toUpperCase() + word.slice(1);
    });
    return result.join("");
};
