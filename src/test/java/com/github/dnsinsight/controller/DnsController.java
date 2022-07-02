package com.github.dnsinsight.controller;

import com.github.dnsinsight.service.DnsService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.BDDMockito.given;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;


/**
 * @Author: Tachikoma
 * @Date: 2022-07-02 11:32
 * @Description:
 */
@WebMvcTest
class TestDnsController {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private DnsService dnsService;

    @Test
    void should_return_ok_when_find_nds_info() throws Exception {
        String dns = "www.baidu.com";
        given(dnsService.findDnsInfo(any())).willReturn(null);

                mockMvc
                .perform(
                        post("/dns-info")
                )
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.questionId").value(1))
        ;
    }

}