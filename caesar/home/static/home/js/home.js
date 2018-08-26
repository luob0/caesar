$(function(){
 var timer = null,
 curindex = 0,
 duration = 2000,
 speed = 500;
 var $imgWrap = $('#slideshow>ul');
 var totalIndex = $imgWrap.find('li').length;
 var width = $('#slideshow').width();
 //insert navigate span, let img in order
 $('#slideshow').find('ul>li').each(function(index){
 $(this).css('left', width*index + 'px');
 $('#slideshow-nav').append('<span>' + (index+1) + '</span>');
 })
 //
 $('#slideshow-nav>span').eq(0).addClass('active');
 //auto slide
 var move = function(){
 curindex += 1;
 if (curindex===totalIndex) {
 curindex = 0;
 }
 // current span add classname "active"
 $('#slideshow-nav>span').each(function(index) {
 $(this).removeClass('active')
 }).eq(curindex).addClass('active');
 //auto slide
 $imgWrap.animate({
 'left': width*curindex*(-1)+'px',
 }, speed)

 timer = setTimeout(move,duration+speed);
 };
 //init
 timer = setTimeout(move,duration);
 //click event
 $('#slideshow-nav>span').on('click', function(event) {
 event.preventDefault();
 /* Act on the event */
 clearTimeout(timer);
 $imgWrap.stop(true, true);
 curindex = $(this).index() - 1;
 move();
 });
 })
 
	$(function(){
		$('#fullpage').fullpage();
    });










