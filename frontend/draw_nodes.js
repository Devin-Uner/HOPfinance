var canvas = document.getElementById("world_canvas");
ctx = canvas.getContext("2d")

var data = {"AAPL.csv": {"GOOG.csv": 0.2778698224852072, "UTHR.csv": 0.24337278106508886, "TSLA.csv": 0.31226331360946713, "MSFT.csv": 0.2959911242603549, "F.csv": 0.19449704142011828, "MMM.csv": 0.20951183431952652, "IBM.csv": 0.2511686390532544, "AMZN.csv": 0.1966715976331361, "INTC.csv": 0.2558136094674558, "DAL.csv": 0.18758875739644973, "SHLD.csv": 0.08579881656804729, "CAT.csv": 0.3148224852071009}, "GOOG.csv": {"AAPL.csv": 0.2778698224852072, "UTHR.csv": 0.22818047337278102, "TSLA.csv": 0.22005177514792892, "MSFT.csv": 0.3555103550295856, "F.csv": 0.15930473372781076, "MMM.csv": 0.23153106508875726, "IBM.csv": 0.2718417159763316, "AMZN.csv": 0.3056139053254441, "INTC.csv": 0.23994822485207107, "DAL.csv": 0.18710798816568036, "SHLD.csv": 0.10079881656804728, "CAT.csv": 0.27789940828402354}, "UTHR.csv": {"AAPL.csv": 0.24337278106508886, "GOOG.csv": 0.22818047337278102, "TSLA.csv": 0.2067529585798817, "MSFT.csv": 0.16700443786982236, "F.csv": 0.12217455621301777, "MMM.csv": 0.13755177514792902, "IBM.csv": 0.13422337278106525, "AMZN.csv": 0.19089497041420123, "INTC.csv": 0.15901627218934924, "DAL.csv": 0.09851331360946751, "SHLD.csv": 0.13594674556213027, "CAT.csv": 0.13047337278106508}, "TSLA.csv": {"AAPL.csv": 0.31226331360946713, "GOOG.csv": 0.22005177514792892, "UTHR.csv": 0.2067529585798817, "MSFT.csv": 0.21244452662721883, "F.csv": 0.18531804733727816, "MMM.csv": 0.19252588757396458, "IBM.csv": 0.2941309171597633, "AMZN.csv": 0.2355436390532546, "INTC.csv": 0.18075813609467448, "DAL.csv": 0.22627588757396444, "SHLD.csv": 0.06797337278106512, "CAT.csv": 0.27908284023668667}, "MSFT.csv": {"AAPL.csv": 0.2959911242603549, "GOOG.csv": 0.3555103550295856, "UTHR.csv": 0.16700443786982236, "TSLA.csv": 0.21244452662721883, "F.csv": 0.19956360946745566, "MMM.csv": 0.33660133136094667, "IBM.csv": 0.3320377218934913, "AMZN.csv": 0.20382026627218963, "INTC.csv": 0.30697855029585774, "DAL.csv": 0.20862056213017766, "SHLD.csv": 0.09821005917159763, "CAT.csv": 0.307662721893491}, "F.csv": {"AAPL.csv": 0.19449704142011828, "GOOG.csv": 0.15930473372781076, "UTHR.csv": 0.12217455621301777, "MSFT.csv": 0.19956360946745566, "TSLA.csv": 0.18531804733727816, "MMM.csv": 0.24253698224852094, "IBM.csv": 0.21367603550295863, "AMZN.csv": 0.2209689349112427, "INTC.csv": 0.19045118343195278, "DAL.csv": 0.26426775147928977, "SHLD.csv": 0.11023668639053262, "CAT.csv": 0.2558875739644968}, "MMM.csv": {"AAPL.csv": 0.20951183431952652, "GOOG.csv": 0.23153106508875726, "UTHR.csv": 0.13755177514792902, "TSLA.csv": 0.19252588757396458, "MSFT.csv": 0.33660133136094667, "F.csv": 0.24253698224852094, "IBM.csv": 0.29361316568047385, "AMZN.csv": 0.16280695266272188, "INTC.csv": 0.25151257396449717, "DAL.csv": 0.16682322485207096, "SHLD.csv": 0.10886094674556218, "CAT.csv": 0.35721893491124274}, "IBM.csv": {"AAPL.csv": 0.2511686390532544, "GOOG.csv": 0.2718417159763316, "UTHR.csv": 0.13422337278106525, "TSLA.csv": 0.2941309171597633, "MSFT.csv": 0.3320377218934913, "F.csv": 0.21367603550295863, "MMM.csv": 0.29361316568047385, "AMZN.csv": 0.213761094674556, "INTC.csv": 0.241830621301775, "DAL.csv": 0.1398631656804734, "SHLD.csv": 0.06170118343195268, "CAT.csv": 0.3232544378698223}, "AMZN.csv": {"AAPL.csv": 0.1966715976331361, "GOOG.csv": 0.3056139053254441, "UTHR.csv": 0.19089497041420123, "MSFT.csv": 0.20382026627218963, "F.csv": 0.2209689349112427, "MMM.csv": 0.16280695266272188, "IBM.csv": 0.213761094674556, "TSLA.csv": 0.2355436390532546, "INTC.csv": 0.1027255917159763, "DAL.csv": 0.08001849112426038, "SHLD.csv": 0.022618343195266264, "CAT.csv": 0.19736686390532546}, "INTC.csv": {"AAPL.csv": 0.2558136094674558, "GOOG.csv": 0.23994822485207107, "UTHR.csv": 0.15901627218934924, "MSFT.csv": 0.30697855029585774, "F.csv": 0.19045118343195278, "MMM.csv": 0.25151257396449717, "IBM.csv": 0.241830621301775, "AMZN.csv": 0.1027255917159763, "TSLA.csv": 0.18075813609467448, "DAL.csv": 0.1900702662721892, "SHLD.csv": 0.08971893491124253, "CAT.csv": 0.2736094674556215}, "DAL.csv": {"AAPL.csv": 0.18758875739644973, "GOOG.csv": 0.18710798816568036, "UTHR.csv": 0.09851331360946751, "TSLA.csv": 0.22627588757396444, "MSFT.csv": 0.20862056213017766, "F.csv": 0.26426775147928977, "MMM.csv": 0.16682322485207096, "IBM.csv": 0.1398631656804734, "AMZN.csv": 0.08001849112426038, "INTC.csv": 0.1900702662721892, "SHLD.csv": 0.09193786982248518, "CAT.csv": 0.18798816568047347}, "SHLD.csv": {"AAPL.csv": 0.08579881656804729, "GOOG.csv": 0.10079881656804728, "UTHR.csv": 0.13594674556213027, "TSLA.csv": 0.06797337278106512, "MSFT.csv": 0.09821005917159763, "F.csv": 0.11023668639053262, "MMM.csv": 0.10886094674556218, "IBM.csv": 0.06170118343195268, "AMZN.csv": 0.022618343195266264, "INTC.csv": 0.08971893491124253, "DAL.csv": 0.09193786982248518, "CAT.csv": 0.15304733727810646}, "CAT.csv": {"AAPL.csv": 0.3148224852071009, "GOOG.csv": 0.27789940828402354, "UTHR.csv": 0.13047337278106508, "TSLA.csv": 0.27908284023668667, "MSFT.csv": 0.307662721893491, "F.csv": 0.2558875739644968, "MMM.csv": 0.35721893491124274, "IBM.csv": 0.3232544378698223, "AMZN.csv": 0.19736686390532546, "INTC.csv": 0.2736094674556215, "DAL.csv": 0.18798816568047347, "SHLD.csv": 0.15304733727810646}}
var wanted = "datasets/GOOG.csv";
var max_radius = 50;
let cell_width = 40;

//make the grid
var DIMENSION = 10;
var X = DIMENSION;
var Y = DIMENSION;
var grid = [[]];
for (var x = 0; x < X; x++) {
	for (var y = 0; y < Y; y++) {
		grid[grid.length-1].push(null);
	}
	grid.push([]);
}
grid.pop();

// generate the circles and give them randomized locations
circles = get_circle_locations();


// draws a circle
// @param string color: a hexidecimal color value for the circle
// @param int x: the x coord for it
// @param int y: the y coord for it
// @param int r: the radius of the circle
function draw_circle(color, x, y, r){
	ctx.lineWidth = 1;
	ctx.strokeStyle = color;
	ctx.fillStyle = color;

	ctx.moveTo(x, y);
	ctx.beginPath();
	ctx.arc(x,y,r,0,2*Math.PI);
	ctx.fill();
	ctx.stroke();

}

// draws a line
function draw_line(color, width, x1, y1, x2, y2){
	ctx.lineWidth = width;
	ctx.strokeStyle = color;
	
	ctx.beginPath();
	ctx.moveTo(x1, y1);
	ctx.lineTo(x2, y2);

	ctx.stroke();
}


// gets the keys of a dictionary
function get_keys(dict){
	var keys = [];
	for(var key in dict)
		keys.push(key);
	return keys;
}

// sorts a dictionary based on its values
// returns the keys from lowest value to highest value
function sort(dict){
	var sorted = [];
	var keys = get_keys(dict);
	var min = null;
	while(sorted.length < keys.length){
		min = null;
		for (var i = 0; i < keys.length; i++) {
			if((min == null || dict[keys[i]] < dict[min]) && sorted.indexOf(keys[i]) == -1)
				min = keys[i];
		}
		sorted.push(min);
	}
	return sorted;
}

// gets the size the circle should be for a given company
function get_size(name){
	var sum = 0;
	var keys = get_keys(data[name]);
	for (var i = 0; i < keys.length; i++) {
		sum += data[name][keys[i]];
	}
	return sum * max_radius / keys.length;
}

// makes the array of where the circles need to go
function get_circle_locations(){

	// step one: get a list of circles to place
	var circles = [];
	var keys = get_keys(data);
	for (var i = 0; i < keys.length; i++) {

		var secondary_keys = get_keys(data[keys[i]]);
		var sum = 0;
		for (var j = 0; j < keys.length; j++) {
			sum += data[keys[i]][keys[j]];
		}

		circles.push([keys[i], get_size(keys[i])]);
	}
	console.log(circles);

	// step two: randomly place circles in the array
	all_circles = [];
		for (var i = 0; i < circles.length; i++) {
            //make sure no two circles are in same cell
            while(true) {
                var randY = Math.floor((Math.random() * DIMENSION));
                if (grid[randX][randY] == null) {
                    break;
                }
            }
            grid[randX][randY] = {"name": circles[i][0], "radius": circles[i][1], "x": randX*max_radius*2 + max_radius, "y": randY*max_radius*2 + max_radius} ;//circles[i];
            all_circles.push({"name": circles[i][0], "radius": circles[i][1], "x": randX*max_radius*2 + max_radius, "y": randY*max_radius*2 + max_radius});
        }
        console.log(grid);

        return all_circles;

}

// randomly moves each circle in the grid
function move_circles(grid){
	let grid_size = max_radius*2;

	// for everything row in the array
	for (var x = 0; x < grid.length; x++) {
		
		// for every cell in the row
		for (var y = 0; y < grid[x].length; y++) {
			
			// if the cell isnt empty
			if(grid[x][y] != null){
				// pick to randomly add or subtract from the x position
				var delta_x = Math.random() > 0.5 ? -1 : 1;
				if(grid[x][y]["x"] + delta_x < 0 || grid[x][y]["x"] + delta_x > (x+1)*grid_size)
					delta_x *= -1;
				grid[x][y]["x"] += delta_x;

				// pick to randomly add or subtract from the y position
				var delta_y = Math.random() > 0.5 ? -1 : 1;
				if(grid[x][y]["y"] + delta_y < 0 || grid[x][y]["y"] + delta_y > (y+1)*grid_size)
					delta_y *= -1;
				grid[x][y]["y"] += delta_y;
			}
		}
	}
}


// draws all the circles to the screen
function draw_circles(grid) {

	// for everything row in the array
	for (var x = 0; x < grid.length; x++) {
		
		// for every cell in the row
		for (var y = 0; y < grid[x].length; y++) {
			
			// if the cell isnt empty
			if(grid[x][y] != null){
				draw_circle("#3F3", grid[x][y]["x"], grid[x][y]["y"], grid[x][y]["radius"]);
			}
		}
	}
}

// draws a line from one company to another
function draw_line_from_companies(name1, name2) {
	 let loc1 = get_location(name1);
	 let loc2 = get_location(name2);

	 let width = Math.floor(data[name1][name2]);
	 console.log(loc1, loc2);
	 draw_line("#0F0", width, loc1[0], loc1[1], loc2[0], loc2[1]);
}



// find the location of any given named circle
function get_location(name){
	for (var i = 0; i < circles.length; i++) {
		if(circles[i]["name"] == name)
			return [circles[i]["x"], circles[i]["y"]];
	}
	return null;
}

//find which edges to draw between circles
function connect_edges() {
    for (int i = 0; i < get_keys(data).length; i++) {
        var sortArr = sort(data[get_keys(data)[i]]);
        for (j = sortArr.length - 1; j > sortArr.length - 4; j--) {
            draw_line_from_companies(get_keys(data)[i], sortedArr[j]);
        } 
    }
}

draw_line_from_companies("AAPL.csv", "GOOG.csv");

/* Compute "diffusion" process. 
 * Takes in one node that gets clicked on.
 * Then uses edge weights to calculate how 
 * "brightness" on other nodes are effected.
 * which determines how closely related two 
 * companies/industries are. */
function graph_reaction(name) {
    var circles = {};
    for(var key in data) {
        circles[key] = 0;
    }
        circles[name] = 100;

    newCircles = copy_dict(circles);
    spread = [];
    while (spread.length < get_keys(circles).length) {
        for (var circ in circles) {
            if (circles[circ] != 0 && spread[circ] != -1) {
                newCircles[circ] = circles[circ];
                newCircles[circ] = sort(data[circ]);
                for (var i = data[circ].length - 1; i > data[circ].length - 4; i--) {
                    newCircles[i] += data[circ][i];
                }
                spread.push(circ); 
            }
            circles = copy_dict(circles);
        }
    }  
}

/* Helper method to copy a dictionary. */
function copy_dict(dict) {
    var copy = {};
    for (entry in dict) {
        copy[entry] = dict[entry];
    }
    return copy;
}























