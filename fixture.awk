BEGIN { 
    FS = "|"; 
    secperday=24*60*60;
    oneyear=365*secperday;
    start2011=41*365*secperday;
    count=1;    
}

{

    createdate = int(start2011+(rand()*oneyear));

    modifydate = int(createdate + (secperday * 31 * rand()))
    publishdate = int(modifydate + (secperday * 31 * rand()))

    print "- model: blog.Blog"
    print "  pk: " count++
    print "  fields:"
    print "    username: graham"
    print "    create_date: '" strftime("%Y-%m-%d %T", createdate) "'"
    print "    modify_date: '" strftime("%Y-%m-%d %T", modifydate) "'"
    print "    blog_title: " $1
    print "    blog_text: " $2

    #print "    published_date: " ((rand() <= 0.5) ? "" : strftime("'%Y-m-d %T'", publishdate))
    if(rand() <= 0.5)  print strftime("    published_date: '%Y-%m-%d %T'", publishdate)

}