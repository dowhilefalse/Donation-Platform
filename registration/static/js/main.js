(function () {

	'use strict';

	var isMobile = {
		Android: function () {
			return navigator.userAgent.match(/Android/i);
		},
		BlackBerry: function () {
			return navigator.userAgent.match(/BlackBerry/i);
		},
		iOS: function () {
			return navigator.userAgent.match(/iPhone|iPad|iPod/i);
		},
		Opera: function () {
			return navigator.userAgent.match(/Opera Mini/i);
		},
		Windows: function () {
			return navigator.userAgent.match(/IEMobile/i);
		},
		any: function () {
			return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
		}
	};

	var mobileMenuOutsideClick = function () {

		$(document).click(function (e) {
			var container = $("#fh5co-offcanvas, .js-fh5co-nav-toggle");
			if (!container.is(e.target) && container.has(e.target).length === 0) {

				if ($('body').hasClass('offcanvas')) {

					$('body').removeClass('offcanvas');
					$('.js-fh5co-nav-toggle').removeClass('active');

				}


			}
		});

	};


	var offcanvasMenu = function () {

		$('#page').prepend('<div id="fh5co-offcanvas" />');
		$('#page').prepend('<a href="#" class="js-fh5co-nav-toggle fh5co-nav-toggle fh5co-nav-white"><i></i></a>');
		var clone1 = $('.menu-1 > ul').clone();
		$('#fh5co-offcanvas').append(clone1);
		var clone2 = $('.menu-2 > ul').clone();
		$('#fh5co-offcanvas').append(clone2);

		$('#fh5co-offcanvas .has-dropdown').addClass('offcanvas-has-dropdown');
		$('#fh5co-offcanvas')
			.find('li')
			.removeClass('has-dropdown');

		// Hover dropdown menu on mobile
		$('.offcanvas-has-dropdown').mouseenter(function () {
			var $this = $(this);

			$this
				.addClass('active')
				.find('ul')
				.slideDown(500, 'easeOutExpo');
		}).mouseleave(function () {

			var $this = $(this);
			$this
				.removeClass('active')
				.find('ul')
				.slideUp(500, 'easeOutExpo');
		});


		$(window).resize(function () {

			if ($('body').hasClass('offcanvas')) {

				$('body').removeClass('offcanvas');
				$('.js-fh5co-nav-toggle').removeClass('active');

			}
		});
	};


	var burgerMenu = function () {

		$('body').on('click', '.js-fh5co-nav-toggle', function (event) {
			var $this = $(this);


			if ($('body').hasClass('overflow offcanvas')) {
				$('body').removeClass('overflow offcanvas');
			} else {
				$('body').addClass('overflow offcanvas');
			}
			$this.toggleClass('active');
			event.preventDefault();

		});
	};


	var contentWayPoint = function () {
		var i = 0;
		$('.animate-box').waypoint(function (direction) {

			if (direction === 'down' && !$(this.element).hasClass('animated-fast')) {

				i++;

				$(this.element).addClass('item-animate');
				setTimeout(function () {

					$('body .animate-box.item-animate').each(function (k) {
						var el = $(this);
						setTimeout(function () {
							var effect = el.data('animate-effect');
							if (effect === 'fadeIn') {
								el.addClass('fadeIn animated-fast');
							} else if (effect === 'fadeInLeft') {
								el.addClass('fadeInLeft animated-fast');
							} else if (effect === 'fadeInRight') {
								el.addClass('fadeInRight animated-fast');
							} else {
								el.addClass('fadeInUp animated-fast');
							}

							el.removeClass('item-animate');
						}, k * 200, 'easeInOutExpo');
					});

				}, 100);

			}

		}, { offset: '85%' });
	};


	var dropdown = function () {

		$('.has-dropdown').mouseenter(function () {

			var $this = $(this);
			$this
				.find('.dropdown')
				.css('display', 'block')
				.addClass('animated-fast fadeInUpMenu');

		}).mouseleave(function () {
			var $this = $(this);

			$this
				.find('.dropdown')
				.css('display', 'none')
				.removeClass('animated-fast fadeInUpMenu');
		});

	};


	var goToTop = function () {

		$('.js-gotop').on('click', function (event) {

			event.preventDefault();

			$('html, body').animate({
				scrollTop: $('html').offset().top
			}, 500, 'easeInOutExpo');

			return false;
		});

		$(window).scroll(function () {

			var $win = $(window);
			if ($win.scrollTop() > 200) {
				$('.js-top').addClass('active');
			} else {
				$('.js-top').removeClass('active');
			}

		});

	};


	// Loading page
	var loaderPage = function () {
		$(".fh5co-loader").fadeOut("slow");
	};

	var counter = function () {
		$('.js-counter').countTo({
			formatter: function (value, options) {
				return value.toFixed(options.decimals);
			},
		});
	};


	var counterWayPoint = function () {
		if ($('#fh5co-counter').length > 0) {
			$('#fh5co-counter').waypoint(function (direction) {

				if (direction === 'down' && !$(this.element).hasClass('animated')) {
					setTimeout(counter, 400);
					$(this.element).addClass('animated');
				}
			}, { offset: '90%' });
		}
	};

	var sliderMain = function () {

		$('#fh5co-hero .flexslider').flexslider({
			animation: "fade",
			slideshowSpeed: 5000,
			directionNav: true,
			start: function () {
				setTimeout(function () {
					$('.slider-text').removeClass('animated fadeInUp');
					$('.flex-active-slide').find('.slider-text').addClass('animated fadeInUp');
				}, 500);
			},
			before: function () {
				setTimeout(function () {
					$('.slider-text').removeClass('animated fadeInUp');
					$('.flex-active-slide').find('.slider-text').addClass('animated fadeInUp');
				}, 500);
			}

		});

	};

	var bibleVerseCarousel = function () {

		var owl = $('.owl-carousel-fullwidth');
		owl.owlCarousel({
			animateOut: 'fadeOut',
			autoplay: true,
			items: 1,
			loop: true,
			margin: 0,
			nav: false,
			dots: true,
			smartSpeed: 800,
			autoHeight: true
		});

	};

	function get_organizations() {
		var unit_box = $(".unit-box")
		var html = ""

		$.get(GLOGAL.API_BASE + "organizations", function (data, status) {
			if (status === 'success') {
				for (var i of data.results) {
					console.log(i)
					html += `<div class="unit">
					<ul style="list-style: none; font-size:18px; color: rgb(75, 75, 75)">
						<li>
							<p>${i.name}</p>
						</li>

						<li>
							<p>省份：${i.province}</p>
						</li>
						<li>
							<p>城市：${i.city}</p>
						</li>
						<li>
						<p>地址：${i.address}</p>
						</li>`
					if (i.demands.length) {
						for (var demand of i.demands) {
							html += `<li>
							<p style="color: red;">需求：${demand.name}
							<span style="color:rgb(75, 75, 75)"> (共需：${demand.amount}、已收${demand.receive_amount})</span></p>
							<p>备注：${demand.remark?demand.remark:'无'}</p>
						</li>`
						}
					}

					for (var contact of i.contacts) {
						html += `<li>
							<p>联系人：${contact.name}</p>
							<p>联系电话：${contact.phone}</p>
						</li>`
					}

					html += `<li>
                    <p>发布日期：2020-01-31</p>
                </li>
				<li>
					${i.verified ? '<p style="color: green">已核实</p>' : '<p style="color: red">未核实</p>'}
				</li>
				</ul>
        		</div>
				`
				}


				unit_box.append(html)



			} else {
				alert('获取数据失败！')
			}
		});
		console.log($(".unit-box"))
	}

    function get_organizations_withindex() {
		var unit_box_index = $(".unit-box-index")
		var html = ""

		$.get(GLOGAL.API_BASE + "organizations", function (data, status) {
			if (status === 'success') {
				for (var i of data.results) {
// 					console.log(i)
					html += `<div class="unit-index">
					<ul style="list-style: none; font-size:18px; color: rgb(75, 75, 75)">
						<li>
							<p id="name">${i.name}</p>
						</li>

						<li>
							省份：<p id="province">${i.province}</p>
						</li>
						<li>
							城市：<p id="city">${i.city}</p>
						</li>
						<li>
						<p>地址：${i.address}</p>
						</li>`
					if (i.demands.length) {
						for (var demand of i.demands) {
							html += `<li>
							<p style="color: red;">需求：${demand.name}
							<span style="color:rgb(75, 75, 75)"> (共需：${demand.amount}、已收${demand.receive_amount})</span></p>
							<p>备注：${demand.remark?demand.remark:'无'}</p>
						</li>`
						}
					}

					for (var contact of i.contacts) {
						html += `<li>
							<p>联系人：${contact.name}</p>
							<p>联系电话：${contact.phone}</p>
						</li>`
					}

					html += `<li>
                    <p>发布日期：2020-01-31</p>
                </li>
				<li>
					${i.verified ? '<p style="color: green">已核实</p>' : '<p style="color: red">未核实</p>'}
				</li>
				</ul>
        		</div>
				`
				}


				unit_box_index.append(html)



			} else {
				alert('获取数据失败！')
			}
		});
		console.log($(".unit-box-index"))
	}
    
    function get_organizations_table_withindex() {
        var unit_table_index = $(".unit-table-index")
		var html = ""

		$.get(GLOGAL.API_BASE + "organizations", function (data, status) {
			if (status === 'success') {
                html += `  <table onload="myFunction()" style="border-collapse: collapse;">
                            <caption style="font-size: larger;         
                             margin: 1em auto;  ">募捐列表信息</caption>

                            <thead>
                                <tr>
                                    <th>医院名称</th>                                                
                                    <th>省份</th>
                                    <th>城市</th>
                                    <th>地址</th>
                                    <th>需求</th>
                                    <th>联系人</th>
                                    <th>是否验证/核实信息过</th>
                               </tr>
                            </thead>
                            <tbody>`
				for (var i of data.results) {
                    html += `
                        <tr>
                            <td>${ i.name }</td>
                            <td>${ i.province }</td>
                            <td>${ i.city }</td>
                            <td>${ i.address }</td>
                            <td>${ i.demands }</td>
                            <td>${ i.contacts }</td>
                            <td>${ i.verified ? '已核实' : '未核实'}</td>
                        </tr>`}
                html += `</tbody>
                         </table>`

				unit_table_index.append(html)
			} else {
				alert('获取数据失败！')
			}
		});
		console.log($(".unit-table-index"))
	}

	$(function () {
		mobileMenuOutsideClick();
		offcanvasMenu();
		burgerMenu();
		contentWayPoint();
		sliderMain();
		dropdown();
		goToTop();
		loaderPage();
		counterWayPoint();
		bibleVerseCarousel();
		get_organizations();
        get_organizations_withindex();
        get_organizations_table_withindex();
	});
    
}());



 