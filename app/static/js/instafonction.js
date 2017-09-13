var userFeed = new Instafeed({
    get: 'user',
    userId: '4209624045',
    accessToken: '4209624045.1677ed0.a0c333c3e7cb4a5b9726e33c51820bd4',
    template: "<a href='{{link}}' target='_blank' id='{{id}}'><img src='{{image}}' /></a>",
    limit: 18
});
userFeed.run();
