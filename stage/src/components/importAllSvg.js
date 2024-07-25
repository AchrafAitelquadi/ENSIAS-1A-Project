function importAll(r) {
    let icons = {};
    r.keys().forEach((item, index) => {
        icons[item.replace('./', '').replace('.svg', '')] = r(item);
    });
    return icons;
}

const icons = importAll(require.context('../assets/icons', false, /\.svg$/));

export default icons;
