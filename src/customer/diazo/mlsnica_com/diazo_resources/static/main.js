function center_logo_url() {
    link = $("#portal-logo").attr("href");
    $(".center-logo a").attr("href" , link);
}
$(document).ready(function() {
	if($(".center-logo").length >0){
		center_logo_url();
	}
});
