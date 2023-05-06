console.clear();

            // 기존 버튼형 슬라이더
            $('.slider-1 > .page-btns > div').click(function () {
                let $this = $(this);
                let index = $this.index();

                $this.addClass('active');
                $this.siblings('.active').removeClass('active');

                let $slider = $this.parent().parent();

                let $current = $slider.find(' > .slides > div.active');

                let $post = $slider.find(' > .slides > div').eq(index);

                $current.removeClass('active');
                $post.addClass('active');
            });

            // 좌/우 버튼 추가 슬라이더
            $('.slider-1 > .side-btns > div').click(function () {
                let $this = $(this);
                let $slider = $this.closest('.slider-1');

                let index = $this.index();
                let isLeft = index == 0;

                let $current = $slider.find(' > .page-btns > div.active');
                let $post;

                if (isLeft) {
                    $post = $current.prev();
                }
                else {
                    $post = $current.next();
                };

                if ($post.length == 0) {
                    if (isLeft) {
                        $post = $slider.find(' > .page-btns > div:last-child');
                    }
                    else {
                        $post = $slider.find(' > .page-btns > div:first-child');
                    }
                };

                $post.click();
            });

            setInterval(function () {
                $('.slider-1 > .side-btns > div').eq(1).click();
            }, 5000);
