<?php $url = "https://sitoscuolamagnifica.altervista.org/TPSIT/index.php";
$page = file_get_contents($url);
$outfile = "copy.html";
file_put_contents($outfile, $page);
$outfile;
/**
 * $url="https://steamcommunity.com/market/search?appid=252490";
 * div#id="searchResultsRows"->foreach(a.class="market_listing_row_link"){href}
 * 
 * numero di pagine span#id="searchResults_links"->foreach(span.class="market_paging_pagelink"){contenuto}
 * inserire nell'url #p1_popular_desc a #p{numero di pagine}_popular_desc
 * 
 * Titolo dell'oggetto : h1#id="largeiteminfo_item_name"{contenuto}
 * Div con img -> div.class="market_listing_largeimage"->img{src}
 * Venduti nelle last 24 : div.class="es_sold_amount"->span.class="market_commodity_orders_header_promote"{contenuto}
 * tabella prezzi vendita : div#id="market_commodity_forsale_table" -> table.class="market_commodity_orders_table"
 * tabella prezzi ordini : div#id="market_commodity_buyreqeusts_table" -> table.class="market_commodity_orders_table"
 */