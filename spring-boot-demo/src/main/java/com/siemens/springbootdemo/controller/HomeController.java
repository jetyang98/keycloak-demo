package com.siemens.springbootdemo.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author yyj
 * @date 2021-10-18 14:55
 */
@RestController
public class HomeController {
    @RequestMapping("/")
    public String index() {
        return "index";
    }

    @RequestMapping("/customer")
    public String customer() {
        return "only customer can see";
    }

    @RequestMapping("/admin")
    public String admin() {
        return "only admin can see";
    }
}
