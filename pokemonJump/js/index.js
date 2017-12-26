//游戏灵感，部分素材来自：Doodle Jump，Pokemon Go

// 用requestAnimFrame绘制60帧动画
window.requestAnimFrame = (function() {
    return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame ||
        function(callback) {
            window.setTimeout(callback, 1000 / 60);
        };
})();

var canvas = document.getElementById('canvas'),
    ctx = canvas.getContext('2d');

var width = 400,
    height = 600;

canvas.width = width;
canvas.height = height;

//初始化
var platforms = [],
    image = document.getElementById("sprite"),
    player, platformCount = 10,
    position = 0,
    gravity = 0.2,
    animloop,
    flag = 0,
    menuloop, broken = 0,
    dir, score = 0,
    firstRun = true,
    //pokemon进化列表参数，默认小火龙
    pokemon = new Array("img/mainxhl1.png", "img/mainxhl2.png", "img/mainxhl3.png", "img/mainmwzz1.png", "img/mainmwzz2.png", "img/mainmwzz3.png", "img/mainjng1.png", "img/mainjng2.png", "img/mainjng3.png"),
    indexStart = 0,
    index = indexStart;

//网格对象
var Base = function() {

    hideElolutionMenu();
    if (indexStart == 0) canvas.style.background = "url(img/bgxhl.png)";
    if (indexStart == 3) canvas.style.background = "url(img/bgmwzz.png)";
    if (indexStart == 6) canvas.style.background = "url(img/bgjng.png)";

    this.height = 5;
    this.width = width;

    this.cx = 0;
    this.cy = 614;
    this.cwidth = 100;
    this.cheight = 5;
    this.moved = 0;

    this.x = 0;
    this.y = height - this.height;

    this.draw = function() {
        ctx.drawImage(image, this.cx, this.cy, this.cwidth, this.cheight, this.x, this.y, this.width, this.height);
    };
};

var base = new Base();

//角色对象
var Player = function() {
    //进化函数
    function evolution() {
        index += 1;
        image.src = pokemon[index];
        showElolutionMenu();
        setTimeout(hideElolutionMenu, 500);
    }
    this.vy = 11;
    this.vx = 0;
    // 左右移动flag
    this.isMovingLeft = false;
    this.isMovingRight = false;
    // 掉落flag
    this.isDead = false;

    this.width = 55;
    this.height = 40;

    this.cx = 0;
    this.cy = 0;
    this.cwidth = 110;
    this.cheight = 80;

    this.dir = "left";

    this.x = width / 2 - this.width / 2;
    this.y = height;


    this.draw = function() {
        // 得分超过500，2000时进化
        if (score == 501) evolution();
        if (score == 2001) evolution();
        //裁剪，绘制素材
        if (this.dir == "right") this.cy = 121;
        else if (this.dir == "left") this.cy = 201;
        else if (this.dir == "right_land") this.cy = 289;
        else if (this.dir == "left_land") this.cy = 371;
        ctx.drawImage(image, this.cx, this.cy, this.cwidth, this.cheight, this.x, this.y, this.width, this.height);

    };
    // 跳跃速度
    this.jump = function() {
        this.vy = -8;
    };
    // 弹簧跳速度
    this.jumpHigh = function() {
        this.vy = -16;
    };

};

player = new Player();

//平台生成
function Platform() {
    this.width = 70;
    this.height = 17;

    this.x = Math.random() * (width - this.width);
    this.y = position;

    position += (height / platformCount);

    this.flag = 0;
    this.state = 0;

    this.cx = 0;
    this.cy = 0;
    this.cwidth = 105;
    this.cheight = 31;

    this.draw = function() {

        if (this.type == 1) this.cy = 0;
        else if (this.type == 2) this.cy = 61;
        else if (this.type == 3 && this.flag === 0) this.cy = 31;
        else if (this.type == 3 && this.flag == 1) this.cy = 1000;
        else if (this.type == 4 && this.state === 0) this.cy = 90;
        else if (this.type == 4 && this.state == 1) this.cy = 1000;

        ctx.drawImage(image, this.cx, this.cy, this.cwidth, this.cheight, this.x, this.y, this.width, this.height);
    };

    //关卡设计
    //1: 绿色不动
    //2: 蓝色移动
    //3: 红色陷阱
    //4: 白色消失

    //根据所在分数调整平台出现概率
    if (score >= 3000) this.types = [2, 3, 3, 3, 4, 4, 4, 4];
    else if (score >= 2000 && score < 3000) this.types = [2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4];
    else if (score >= 1000 && score < 2000) this.types = [2, 2, 2, 3, 3, 3, 3, 3];
    else if (score >= 500 && score < 1000) this.types = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3];
    else if (score >= 100 && score < 500) this.types = [1, 1, 1, 1, 2, 2];
    else this.types = [1];

    this.type = this.types[Math.floor(Math.random() * this.types.length)];

    //不能连续出现2个红色平台，用普通平台替换掉
    if (this.type == 3 && broken < 1) {
        broken++;
    } else if (this.type == 3 && broken >= 1) {
        this.type = 1;
        broken = 0;
    }

    this.moved = 0;
    this.vx = 1;
}

for (var i = 0; i < platformCount; i++) {
    platforms.push(new Platform());
}

//红色平台断裂
var Platform_broken = function() {
    this.height = 30;
    this.width = 70;

    this.x = 0;
    this.y = 0;

    this.cx = 0;
    this.cy = 554;
    this.cwidth = 105;
    this.cheight = 60;
    //原平台消失
    this.appearance = false;
    //绘制断裂平台
    this.draw = function() {
        if (this.appearance === true) ctx.drawImage(image, this.cx, this.cy, this.cwidth, this.cheight, this.x, this.y, this.width, this.height);
        else return;
    };
};

var platform_broken = new Platform_broken();

//弹簧对象
var spring = function() {
    this.width = 26;
    this.height = 30;

    this.x = 0;
    this.y = 0;

    this.cx = 0;
    this.cy = 0;
    this.cwidth = 45;
    this.cheight = 53;

    this.state = 0;

    this.draw = function() {
        if (this.state === 0) this.cy = 445;
        else if (this.state == 1) this.cy = 501;
        ctx.drawImage(image, this.cx, this.cy, this.cwidth, this.cheight, this.x, this.y, this.width, this.height);
    };
};

var Spring = new spring();

function init(a) {
    //初始化游戏
    firstRun = false;
    var dir = "left",
        jumpCount = 0;
    indexStart = a;
    reset();
    //刷新画布函数
    function clearCanvas() {
        ctx.clearRect(0, 0, width, height);
    }

    //角色相关
    function playerCalc() {
        if (dir == "left") {
            player.dir = "left";
            if (player.vy < -7 && player.vy > -15) player.dir = "left_land";
        } else if (dir == "right") {
            player.dir = "right";
            if (player.vy < -7 && player.vy > -15) player.dir = "right_land";
        }

        //键盘控制
        document.onkeydown = function(e) {
            var key = e.keyCode;

            if (key == 37) {
                dir = "left";
                player.isMovingLeft = true;
            } else if (key == 39) {
                dir = "right";
                player.isMovingRight = true;
            }
            // 开始或重启游戏
            if (key == 32) {
                if (firstRun === true)
                    init();
                else
                    reset();
            }
        };

        document.onkeyup = function(e) {
            var key = e.keyCode;

            if (key == 37) {
                dir = "left";
                player.isMovingLeft = false;
            } else if (key == 39) {
                dir = "right";
                player.isMovingRight = false;
            }
        };

        //加速度计算，位置计算
        if (player.isMovingLeft === true) {
            player.x += player.vx;
            player.vx -= 0.15;
        } else {
            player.x += player.vx;
            if (player.vx < 0) player.vx += 0.1;
        }

        if (player.isMovingRight === true) {
            player.x += player.vx;
            player.vx += 0.15;
        } else {
            player.x += player.vx;
            if (player.vx > 0) player.vx -= 0.1;
        }

        // 最大速度限制
        if (player.vx > 8) player.vx = 8;
        else if (player.vx < -8) player.vx = -8;

        //跳跃判断
        if ((player.y + player.height) > base.y && base.y < height) player.jump();

        //游戏结束判断 
        if (base.y > height && (player.y + player.height) > height && player.isDead != "yes") player.isDead = true;

        //左右连接
        if (player.x > width) player.x = 0 - player.width;
        else if (player.x < 0 - player.width) player.x = width;

        //重力作用
        if (player.y >= (height / 2) - (player.height / 2)) {
            player.y += player.vy;
            player.vy += gravity;
        }

        //角色到画布中间时移动平台，生成新平台
        else {
            platforms.forEach(function(p, i) {

                if (player.vy < 0) {
                    p.y -= player.vy;
                }

                if (p.y > height) {
                    platforms[i] = new Platform();
                    platforms[i].y = p.y - height;
                }

            });

            base.y -= player.vy;
            player.vy += gravity;

            if (player.vy >= 0) {
                player.y += player.vy;
                player.vy += gravity;
            }

            score++;
        }

        //碰撞跳跃
        collides();

        if (player.isDead === true) gameOver();
    }

    //弹簧算法
    function springCalc() {
        var s = Spring;
        var p = platforms[0];

        if (p.type == 1 || p.type == 2) {
            s.x = p.x + p.width / 2 - s.width / 2;
            s.y = p.y - p.height - 10;

            if (s.y > height / 1.1) s.state = 0;

            s.draw();
        } else {
            s.x = 0 - s.width;
            s.y = 0 - s.height;
        }
    }

    //平台移动，掉落速度算法
    function platformCalc() {
        var subs = platform_broken;

        platforms.forEach(function(p, i) {
            if (p.type == 2) {
                if (p.x < 0 || p.x + p.width > width) p.vx *= -1;

                p.x += p.vx;
            }

            if (p.flag == 1 && subs.appearance === false && jumpCount === 0) {
                subs.x = p.x;
                subs.y = p.y;
                subs.appearance = true;

                jumpCount++;
            }

            p.draw();
        });

        if (subs.appearance === true) {
            subs.draw();
            subs.y += 8;
        }

        if (subs.y > height) subs.appearance = false;
    }

    function collides() {
        //平台
        platforms.forEach(function(p, i) {
            if (player.vy > 0 && p.state === 0 && (player.x + 15 < p.x + p.width) && (player.x + player.width - 15 > p.x) && (player.y + player.height > p.y) && (player.y + player.height < p.y + p.height)) {

                if (p.type == 3 && p.flag === 0) {
                    p.flag = 1;
                    jumpCount = 0;
                    return;
                } else if (p.type == 4 && p.state === 0) {
                    player.jump();
                    p.state = 1;
                } else if (p.flag == 1) return;
                else {
                    player.jump();
                }
            }
        });

        //弹簧
        var s = Spring;
        if (player.vy > 0 && (s.state === 0) &&
            (player.x + 15 < s.x + s.width) &&
            (player.x + player.width - 15 > s.x) &&
            (player.y + player.height > s.y) &&
            (player.y + player.height < s.y + s.height)) {
            s.state = 1;
            player.jumpHigh();
        }

    }
    // 计分
    function updateScore() {
        var scoreText = document.getElementById("score");
        scoreText.innerHTML = score;
    }
    // 游戏结束
    function gameOver() {
        platforms.forEach(function(p, i) {
            p.y -= 12;
        });

        if (player.y > height / 2 && flag === 0) {
            player.y -= 8;
            player.vy = 0;
        } else if (player.y < height / 2) flag = 1;
        else if (player.y + player.height > height) {
            showGoMenu();
            hideScore();
            player.isDead = "yes";
        }
    }

    //初始刷新函数
    function update() {
        clearCanvas();
        playerCalc();
        platformCalc();
        springCalc();
        base.draw();
        player.draw();
        updateScore();
    }

    menuLoop = function() { return; };
    animloop = function() {
        update();
        requestAnimFrame(animloop);
    };

    animloop();

    hideMenu();
    showScore();
}

//重置游戏
function reset() {
    hideGoMenu();
    showScore();
    player.isDead = false;

    index = indexStart;
    image.src = pokemon[index];

    flag = 0;
    position = 0;
    score = 0;

    base = new Base();
    player = new Player();
    Spring = new spring();
    platform_broken = new Platform_broken();

    platforms = [];
    for (var i = 0; i < platformCount; i++) {
        platforms.push(new Platform());
    }
}

//隐藏开始界面
function hideMenu() {
    var menu = document.getElementById("mainMenu");
    menu.style.zIndex = -1;
}

//显示游戏结束界面
function showGoMenu() {
    var menu = document.getElementById("gameOverMenu");
    menu.style.zIndex = 1;
    menu.style.visibility = "visible";

    var scoreText = document.getElementById("go_score");
    scoreText.innerHTML = "得分：" + score;
}

//隐藏游戏结束界面
function hideGoMenu() {
    var menu = document.getElementById("gameOverMenu");
    menu.style.zIndex = -1;
    menu.style.visibility = "hidden";
}

//显示记分板
function showScore() {
    var menu = document.getElementById("scoreBoard");
    menu.style.zIndex = 1;
}

//隐藏记分板
function hideScore() {
    var menu = document.getElementById("scoreBoard");
    menu.style.zIndex = -1;
}

//显示进化
function showElolutionMenu() {
    var menu = document.getElementById("evolutionMenu");
    menu.style.zIndex = 1;
}

//隐藏进化
function hideElolutionMenu() {
    var menu = document.getElementById("evolutionMenu");
    menu.style.zIndex = -1;
}

//跳跃函数
function playerJump() {
    player.y += player.vy;
    player.vy += gravity;

    if (player.vy > 0 &&
        (player.x + 15 < 260) &&
        (player.x + player.width - 15 > 155) &&
        (player.y + player.height > 475) &&
        (player.y + player.height < 500))
        player.jump();

    if (dir == "left") {
        player.dir = "left";
        if (player.vy < -7 && player.vy > -15) player.dir = "left_land";
    } else if (dir == "right") {
        player.dir = "right";
        if (player.vy < -7 && player.vy > -15) player.dir = "right_land";
    }

    //键盘控制
    document.onkeydown = function(e) {
        var key = e.keyCode;

        if (key == 37) {
            dir = "left";
            player.isMovingLeft = true;
        } else if (key == 39) {
            dir = "right";
            player.isMovingRight = true;
        }

        if (key == 32) {
            if (firstRun === true) {
                init();
                firstRun = false;
            } else
                reset();
        }
    };

    document.onkeyup = function(e) {
        var key = e.keyCode;

        if (key == 37) {
            dir = "left";
            player.isMovingLeft = false;
        } else if (key == 39) {
            dir = "right";
            player.isMovingRight = false;
        }
    };

    //速度，加速度控制
    if (player.isMovingLeft === true) {
        player.x += player.vx;
        player.vx -= 0.15;
    } else {
        player.x += player.vx;
        if (player.vx < 0) player.vx += 0.1;
    }

    if (player.isMovingRight === true) {
        player.x += player.vx;
        player.vx += 0.15;
    } else {
        player.x += player.vx;
        if (player.vx > 0) player.vx -= 0.1;
    }

    //碰撞平台跳跃
    if ((player.y + player.height) > base.y && base.y < height) player.jump();

    //左右打通
    if (player.x > width) player.x = 0 - player.width;
    else if (player.x < 0 - player.width) player.x = width;

    player.draw();
}

function update() {
    ctx.clearRect(0, 0, width, height);
    playerJump();
}

// 动画循环函数
menuLoop = function() {
    update();
    requestAnimFrame(menuLoop);
};

menuLoop();

function orientationHandler(event) {
    if (event.gamma <= -5) {
        player.isMovingRight = false;
        player.isMovingLeft = true;
    } else if (event.gamma >= 5) {
        player.isMovingLeft = false;
        player.isMovingRight = true;
    }
}

function motionHandler(event) {
    var acc = event.acceleration;
    var accGravity = event.accelerationIncludingGravity;
    var rotationRate = event.rotationRate;
}

if (window.DeviceMotionEvent) {
    window.addEventListener("devicemotion", motionHandler, false);
} else {
    document.body.innerHTML = "What user agent u r using???";
}

if (window.DeviceOrientationEvent) {
    window.addEventListener("deviceorientation", orientationHandler, false);
} else {
    document.body.innerHTML = "What user agent u r using???";
};