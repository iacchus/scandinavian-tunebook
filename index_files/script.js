
	$(document).ready(function(){

		if($("pre.abctune").length)
		{
			var tunes_code = $("pre.abctune");
				
			for(var $i=0; tunes_code[$i]; $i++)
			{               
				var ws_strip="";
				var mystr="";

				ws_strip = $(tunes_code[$i]).text().split('\n');
				for(var aaa=0; ws_strip[aaa]; aaa++) { mystr+=ws_strip[aaa].trim() + "\n"; }
				
				$(tunes_code[$i]).text(mystr), //abctune

				$('<div id="abctune-' + $i + '" class="abctune-rendered"></div>').insertBefore(tunes_code[$i]);
				ABCJS.renderAbc(
					"abctune-"+$i, //container
					$(tunes_code[$i]).text(), //abctune
					{}, //parserParams
					{ staffwidth: 940,
				          scale: 1.25,
					paddingleft: 0,	paddingright: 0 }, //engraverParams
					{ viewportHorizontal: true } //renderParams
					);
				$(tunes_code[$i]).hide();
			}
		}

	})
