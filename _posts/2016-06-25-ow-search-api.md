---
layout: post
title: 守望屁股全球查询api+js
subtitle: 我才不会说js是偷的（
author: Coink 
date: 2016-06-26 00:00:00 
categories: 
tag: 
- Science
---
守望先锋（ow）全球开服也有一段时间了，作为一个创意并不新鲜的游戏，暴雪无疑是非常成功的，玩家数直破10 million，至于守望先锋为什么这么火，在此不做分析~~因为我也懒得分析啊哈哈哈哈哈~~

这种半休闲游戏不同于CSGO，外加战网的ID系统比Steam更加具有确定性，所以各大网站的OW查询系统分上线，这时候，不正是偷js和api的好时机嘛？不对不对，读书人的事，怎么能叫偷呢？

~~于是我就偷了朋友偷来的查询JS和API地址~~

毕竟暴雪暂时没有开放api，查询还不够准确


```javascript

var searchArr = location.search.replace("?","").split("&"),areaL;
for(var i=0;i<searchArr.length;i++){
	var arr = searchArr[i].split("=");
	if(arr[0]=="name"){
		search = decodeURI(arr[1]);
	}
	if(arr[0]=="areaLink"){
		areaL = decodeURI(arr[1]);
	}
}


//英雄的分类，英雄定位通过英文名与定位分类
var heroType={
	offense:["士兵76","死神","法老之鹰","源氏","猎空","麦克雷"],
	defense:["半藏","堡垒","黑百合","小美","托比昂","狂鼠"],
	tank:["D.Va","路霸","查莉娅","温斯顿","莱因哈特"],
	support:["天使","禅雅塔","卢西奥","秩序之光"]
}
// 无name 返回搜索页
if(!search || !search[0]){
	backSearchPage();
}

var fwq = {
	'国服':'pc/cn/',
	'美服':'pc/us/',
	'欧服':'pc/eu/',
	'亚服':'pc/kr/',
	'PSN':'psn/',
	'XBox':'xbl/',
'pc/cn/':'国服',
	'pc/us/':'美服',
	'pc/eu/':'欧服',
	'pc/kr/':'亚服',
	'psn/':'PSN',
	'xbl/':'XBox'
}

//奖牌排序
var awardSort=["奖牌总数","杰出卡","金牌","银牌","铜牌"];
// 返回搜索页
function backSearchPage(){
	location.href  = "http://ow.766.com/?error";
}

var initData={},
	totle={},
	heros = [],
	name=sessionStorage.ow766name&&sessionStorage.ow766name.replace("#","-");

if(search == name){// 从搜索页过来
	initData = JSON.parse(sessionStorage.ow766data);
	sessionStorage.removeItem("ow766name");
	sessionStorage.removeItem("ow766data")
}else{//直接打开页面，重新获取接口信息
	search = search;
		getJson({
			url:"http://ow.766.com/player/playerDetailByAreaLink",
			timeout:30000,
			data:{
				playerName:search,
				areaLink: fwq[areaL]
			},
			success:function(data){
				var data = JSON.parse(data);
				if(data.httpStatus == "404"||data.httpStatus == "500"){
					backSearchPage();
					return;
				}
				yexiao.showAll = true;
				yexiao.data = data;
			},
			error:function(){
				backSearchPage();
			}
		})
	
}
//avalon定义
var yexiao = avalon.define({
	$id  : "yexiao",
	data : initData,
	name : search.replace(/[\#\-][0-9]+$/,""),
	totle: totle,
	shenglv:function(e1,e2){
		if(Number(e2) == 0){
			return 0
		}
		return parseInt(Number(e1.replace(",",""))*100/Number(e2.replace(",",""))) +"%"
	},
	updataStatus:false,
	update:function(){
		if(!yexiao.updataStatus){
			getJson({
				url:"http://ow.766.com/player/playerDetailByAreaLink",
				timeout:30000,
				data:{
					playerName:search,
					areaLink: areaL,
					isUpdateCache : 1
				},
				success:function(data){
					var data = JSON.parse(data);
					if(data.httpStatus == "404"||data.httpStatus == "500"){
						alert("更新失败！");
						return;
					}
					location.href  = "http://ow.766.com/search?name="+search+"&areaLink="+areaL
				},
				error:function(){
					
				}
			})
			
		}
		yexiao.updataStatus = true;
	},
	times:[],
	orderBy:"对战次数",
	heros:heros,
	hero:[],
	award:[],
	areaLink: fwq[areaL] || "国服",
	getMore:function(){
		var len = yexiao.hero.length,
			all = yexiao.heros.length;
		if(len<10){
			getShowHero(all);
			yexiao.getMoreText = "收起所有英雄";
		}else{
			getShowHero(6);
			yexiao.getMoreText = "查看所有英雄";
		}
	},
	getMoreText:"查看所有英雄",
	order : function(str){
		strs = str.split('.');
		yexiao.orderBy = strs[1];
		yexiao.heros.sort(compare(str));
		if(yexiao.getMoreText=="查看所有英雄"){
			getShowHero(yexiao.hero.length);
		}else{
			getShowHero(yexiao.heros.length);
		}
	},
	getIconFromName :function(name){
		var data = yexiao.data.topHeroMap["命中率"].heroList;
		for(var i=0;i<data.length;i++){
			if(data[i].heroName == name){
				return data[i].heroIcon;
			}
		}
		return ""
	},
	career:{},
	careerBy:"",
	achieveBy:"",
	achieveHasGeted:[],
	achieve:{},
	setState:function(v){
		return v ? 1 : 0.4
	},
	water:function(){
		water();
		window.onresize = function(){
			water()
		}
	},
	to:function(id){
		var obj = document.getElementById(id);
		window.scrollTo(0,obj.offsetTop);
		if(window.outerWidth<768){
			document.getElementById("float").style.display="none";
		}
		
	},
	inputName:"",
	search:function(){
		var name = yexiao.inputName.replace(/\#/i,"-");
		yexiao.showAll = false;
		var are = fwq[yexiao.areaLink];
		getJson({
			url:"http://ow.766.com/player/playerDetailByAreaLink",
			timeout:30000,
			data:{
				playerName:name,
				areaLink: are
			},
			success:function(data){
				var obj = JSON.parse(data);
				if(obj.httpStatus == "404" || obj.httpStatus == "500"){
					backSearchPage();
					return;
				}
				sessionStorage.ow766name = yexiao.inputName;
				sessionStorage.ow766data = data;
				location.href  = "http://ow.766.com/search?name="+name+"&areaLink="+yexiao.areaLink
				//location.href  = "http://127.0.0.1:8020/pro/search.html?name="+name+"&areaLink="+yexiao.areaLink
			},
			error:function(){
				backSearchPage()
			}
		})
		
	},
	showAll:false,
	hasStar:function(){
		return !!yexiao.data.levelStarIcon
	}
})
//监控data变化  调整内部的一个数据
yexiao.$watch("data",function(v){
	yexiao.careerBy = "所有英雄";
	yexiao.achieveBy = "一般";
	yexiao.totle = yexiao.data.statsSectionMap['所有英雄'].statsSectionMap;
	yexiao.heros = getYexiaoHero(yexiao.data.statsSectionMap);
	yexiao.heros.sort(compare('游戏.对战次数'));
	getShowHero(6);
	getAchieveHasGeted();
	getTypeAllTime();
	var data = yexiao.data.statsSectionMap['所有英雄'].statsSectionMap['对战奖励'];
	for(var i=0;i<awardSort.length;i++){
		for(var j in data){
			if(j == awardSort[i]){
				yexiao.award.push({n:j,v:data[j]});
				break;
			}
		}
	}
})
//生涯统计切换
yexiao.$watch("careerBy",function(v){
	yexiao.career = yexiao.data.statsSectionMap[v].statsSectionMap
})
//成就切换
yexiao.$watch("achieveBy",function(v){
	yexiao.achieve = yexiao.data.achievementsSectionMap[v].achList
})

//数据更新
if(!!initData){
    try{
    	yexiao.totle = initData.statsSectionMap&&initData.statsSectionMap['所有英雄'].statsSectionMap;
	    yexiao.heros = getYexiaoHero(initData.statsSectionMap);
	    yexiao.heros.sort(compare('游戏.对战次数'))
	    yexiao.careerBy = "所有英雄";
	    yexiao.achieveBy = "一般";
	    getShowHero(6);
	    getAchieveHasGeted();
	    getTypeAllTime();
	    yexiao.showAll = true;
	    var data = yexiao.data.statsSectionMap['所有英雄'].statsSectionMap['对战奖励'];
		
		for(var i=0;i<awardSort.length;i++){
			for(var j in data){
				if(j == awardSort[i]){
					yexiao.award.push({n:j,v:data[j]});
					break;
				}
			}
		}
    }catch(e){
    	
    }
}

//将英雄统计部分数据转化为数组
function getYexiaoHero(data){
	var heros=[];
	for(var i in data){
		
		if( typeof data[i] == 'function') continue;
		data[i].name = i
		heros.push(data[i])
	}
	return heros;
}

//formatParams
function formatParams(data) {
    var arr = [];
    for (var name in data) {
        arr.push(encodeURIComponent(name) + "=" + encodeURIComponent(data[name]));
    }
    return arr.join("&");
}

//排序
function compare(str) { 
	str = str.split(".");
	return function (object1, object2) { 
		var value1 =(object1.statsSectionMap&&object1.statsSectionMap[str[0]][str[1]]) || "";
		var value2 = (object2.statsSectionMap&&object2.statsSectionMap[str[0]][str[1]]) || ""; 
		value1 = parseInt(value1.replace(",","") || 0);
		value2 = parseInt(value2.replace(",","")|| 0);
		if (value2 < value1) { 
			return -1; 
		} 
		else if (value2 > value1) { 
			return 1; 
		} 
		else { 
			return 0; 
		}
	} 
} 

//获取数据
function getJson(options) {
    options = options || {};
    var params = formatParams(options.data);
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            var status = xhr.status;
            if (status >= 200 && status < 300) {
                options.success && options.success(xhr.responseText);
            } else {
                options.error && options.error(status);
            }
        }
    }
    xhr.open("GET", options.url + "?" + params, true);
    xhr.send(null);
    setTimeout(function(){
    	if(xhr.readyState == 2){
    		alert("数据获取超时，我们也很捉急！请稍后再试！")
    		xhr.abort();
    		options.error && options.error(status);
    	}
    },options.timeout || 10000)
}

//获取已获得成就  综合数据统计中
function getAchieveHasGeted(){
	var arr=[];
	for(var i in yexiao.data.achievementsSectionMap){
		var achieve = yexiao.data.achievementsSectionMap[i];
		if(typeof achieve == 'function') continue;
		for(var j=0;j<achieve.achList.length;j++){
			var ach = achieve.achList[j];
			if(ach.achState){
				arr.push(avalon.mix(ach,{type:i}))
			}
		}
	}
	yexiao.achieveHasGeted = arr;
}
//获取各类型英雄时间
function getTypeAllTime(){
	var times ={
		offense:0,
		defense:0,
		tank:0,
		support:0
	},allTime = 0;
	var data = yexiao.data.statsSectionMap;
	
	for(var type in heroType){
		for(var i=0;i<heroType[type].length;i++){
			if(data[heroType[type][i]]){
				var time = data[heroType[type][i]].statsSectionMap['游戏']['游戏总时间'];
				if(time.indexOf("小时")>=0){
					var timeArr = time.split("小时");
					times[type]+= (parseInt(timeArr[0])*60+parseInt(timeArr[1] || 0))
				}else{
					times[type]+= parseInt(time)
				}
			}
		}
		allTime+=times[type]
	}
	var types= [
		{eName:"offense",cName:"突击"},
		{eName:"defense",cName:"防御"},
		{eName:"tank",cName:"重装"},
		{eName:"support",cName:"支援"}
	],
	average = allTime/4,pers=0,arr=[];
	for(var i=0;i<types.length;i++){
		var type = types[i],
		time = times[type.eName],
		percent = parseInt((time+average)/allTime/2*100),
		time = time >60 ? Math.round(time/60)+"小时" : time+"分钟";
		if(i<types.length-1){
			pers+=percent;
		}else{
			percent = 100-pers;
		}
		
		arr.push({
			time : time,
			percent  : percent,
			cName : type.cName,
			eName : type.eName
		})
	}
	
	
	yexiao.times = arr.sort(compare2('percent'));
	
	
	//排序
function compare2(type) { 
	return function (object1, object2) { 
		var value1 = object1[type];
		var value2 = object2[type]; 
		if (value2 < value1) { 
			return -1; 
		} 
		else if (value2 > value1) { 
			return 1; 
		} 
		else { 
			return 0; 
		}
	} 
} 
}

//英雄统计
function getShowHero(len){
	var j=0;
	yexiao.hero = [];
	for(var i=0;i<yexiao.heros.length;i++){
		if(j>=len){
			return;
		}
		if(yexiao.heros[i].name!=="所有英雄"){
			yexiao.hero.push(yexiao.heros[i]);
			j++;
		}
	}
}

// 顶部search 显隐
function toggleSearch(){
	var cl = document.getElementById("search").className;
	if(cl.indexOf(" slideDown")<0){
		cl = cl.replace("slideUp","");
		document.getElementById("search").className = cl+" slideDown"
	}else{
		cl = cl.replace(" slideDown","");
		document.getElementById("search").className = cl+" slideUp"
	}
}

// float 显影
function toggleFloat(){
	var fs= document.getElementById("float");
	if(fs.style.display=="block"){
		fs.style.display="none"
	}else{
		fs.style.display="block"
	}
}


//瀑布流
function water(){
	var container = document.getElementById("wrap"),
		items = container.getElementsByClassName("item");
		if(items.length<1) return;
	container.style.position="relative";
	var conWidth = container.offsetWidth,
		itemsWidth = items[0].offsetWidth,
		columCount = parseInt(conWidth/itemsWidth);
		
	function flow(){
		var arr=[];
		for(var i=0;i<columCount;i++){
			arr[i] = 0 ;
		}
		for(var i=0;i<items.length;i++){
			var item = items[i],
				height = item.offsetHeight,
				arrH = Math.min.apply(null, arr),
				index,
				j=0;
			for(;j<arr.length;j++){
				if(arr[j] == arrH){
					index = j;
					break;
				}
			}
			item.style.position = 'absolute';
			item.style.left = (Math.round((index/columCount) * 10000)/100).toFixed(2) + '%';
			item.style.top = arr[index] +"px";
			arr[index] +=height ;
			container.style.height = Math.max.apply(null, arr) +"px";
			item = height = arrH = index = j = null;
		}
	}
	flow();
};

```

代码神tm一脸~~噫~~易语言的味道....


