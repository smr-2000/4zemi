 $('.Heart-Inner-Box-Item-LikesIcon').on('click', function() {
    let $btn = $(this);    
    if ($btn.hasClass('on')) {
      $btn.removeClass('on');
      $btn.children("i").attr('class', 'far fa-heart Heart-Inner-Box-Item-LikesIcon-fa-heart');
    } else {
      $btn.addClass('on');
      $btn.children("i").attr('class', 'fas fa-heart Heart-Inner-Box-Item-LikesIcon-fa-heart heart');
    }
 });

