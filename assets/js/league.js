function get_league_icon(league) {
    if(/Bronze/.test(league)) return 'BronzeLeague.png';
    else if(/Champion/.test(league)) return 'ChampionLeague.png';
    else if(/Crystal/.test(league)) return 'CrystalLeague.png';
    else if(/Gold/.test(league)) return 'GoldLeague.png';
    else if(/Legend/.test(league)) return 'LegendLeague.png';
    else if(/Master/.test(league)) return 'MasterLeague.png';
    else if(/Silver/.test(league)) return 'SilverLeague.png';
    else if(/Titan/.test(league)) return 'TitanLeague.png';
    else return 'UnrankedLeague.png';
}
